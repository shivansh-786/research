import os
import json
from typing import Dict, List, Any, TypedDict
from datetime import datetime
from dotenv import load_dotenv
import anthropic
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from retrieval import ZeronRAG  # Import your existing RAG system

# Load environment variables
load_dotenv()

class AgentState(TypedDict):
    """State for the research agent workflow"""
    query: str
    query_type: str
    rag_context: str
    rag_response: Dict[str, Any]
    web_search_results: List[str]
    final_answer: str
    requires_web_search: bool
    search_strategy: str
    confidence_level: str

class ZeronEnhancedRAG:
    """Enhanced research agent using Groq for LLM and Anthropic for web search only"""
    
    def __init__(self):
        print("🚀 Initializing Zeron Enhanced Research Agent...")
        
        # Initialize the existing RAG system
        self.rag_system = ZeronRAG()
        
        # Initialize Groq LLM for all reasoning tasks
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.1
        )
        
        # Initialize Anthropic client ONLY for web search
        self.anthropic_client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        
        self.setup_workflow()
        print("✅ Enhanced Research Agent ready!")
    
    def classify_query(self, state: AgentState) -> AgentState:
        """Simple classification using keyword matching"""
        query = state["query"].lower()
        
        # Web search indicators
        web_keywords = [
            'competitor', 'vs', 'versus', 'compared', 'battle card', 'battlecard',
            'market', 'industry', 'trends', 'top', 'best', 'leaders',
            'pricing', 'cost', 'latest', 'recent', 'news', 'benchmark'
        ]
        
        # Check if web search is needed
        needs_web = any(keyword in query for keyword in web_keywords)
        
        state["requires_web_search"] = needs_web
        state["search_strategy"] = "RAG + Web Search" if needs_web else "RAG Only"
        state["confidence_level"] = "high" if needs_web else "medium"
        state["query_type"] = self._determine_query_type(query, {})
        
        print(f"🧠 Classification: {state['search_strategy']}")
        
        return state
    
    def _determine_query_type(self, query: str, result: dict) -> str:
        """Determine query type for template selection"""
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['battle card', 'vs', 'versus', 'compared']):
            return "battle_card"
        elif any(word in query_lower for word in ['market', 'industry', 'trends', 'analysis']):
            return "market_analysis"
        elif any(word in query_lower for word in ['technical', 'architecture', 'feature']):
            return "technical_comparison"
        else:
            return "general"
    
    def _fallback_classification(self, query: str) -> bool:
        """Fallback classification using simple keyword matching"""
        web_keywords = [
            'competitor', 'vs', 'versus', 'compared', 'battle card', 'battlecard',
            'market', 'industry', 'trends', 'top', 'best', 'leaders',
            'pricing', 'cost', 'latest', 'recent', 'news', 'benchmark'
        ]
        return any(keyword in query.lower() for keyword in web_keywords)
    
    def retrieve_from_rag(self, state: AgentState) -> AgentState:
        """
        Always retrieve relevant context from your vector database
        """
        query = state["query"]
        
        try:
            print(f"🔍 Searching internal vector database...")
            
            # Use your existing RAG system
            rag_response = self.rag_system.query(query)
            state["rag_response"] = rag_response or {}
            
            if rag_response and rag_response.get("source_documents"):
                # Extract context for potential web search enhancement
                context_parts = []
                for doc in rag_response["source_documents"]:
                    category = doc.metadata.get('category', 'Unknown')
                    content = doc.page_content[:400]  # More context for web search
                    context_parts.append(f"[Zeron {category}] {content}")
                
                state["rag_context"] = "\n\n".join(context_parts)
                print(f"✅ Found {len(rag_response['source_documents'])} relevant internal documents")
            else:
                state["rag_context"] = "No relevant internal documentation found."
                print("⚠️ No relevant internal documents found")
            
        except Exception as e:
            print(f"❌ RAG retrieval error: {e}")
            state["rag_response"] = {"answer": f"RAG Error: {str(e)}", "source_documents": []}
            state["rag_context"] = ""
        
        return state
    
    def perform_web_search(self, state: AgentState) -> AgentState:
        """Perform web search using Anthropic"""
        if not state["requires_web_search"]:
            state["web_search_results"] = []
            return state
        
        try:
            query = state["query"]
            internal_context = state["rag_context"]
            
            print(f"🌐 Performing web search for: {query}")
            
            web_search_prompt = f"""
            Search the web for comprehensive information about: "{query}"
            
            Context from Zeron's internal docs:
            {internal_context}
            
            Focus on finding:
            - Competitive analysis and market intelligence
            - Industry trends and benchmarks  
            - Recent developments and news
            - Pricing and feature comparisons
            - Technical specifications and capabilities
            
            Provide a detailed, well-structured summary of your findings.
            """
            
            response = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[{"role": "user", "content": web_search_prompt}],
                tools=[{
                    "type": "web_search_20250305",
                    "name": "web_search"
                }]
            )
            
            if response.content and hasattr(response.content[0], 'text'):
                search_result = response.content[0].text
                state["web_search_results"] = [search_result]
                print("✅ Web search completed")
            else:
                state["web_search_results"] = ["Web search completed with limited results"]
                print("⚠️ Limited web search results")
            
        except Exception as e:
            print(f"❌ Web search error: {e}")
            state["web_search_results"] = [f"Web search error: {str(e)}"]
        
        return state
    
    def synthesize_answer(self, state: AgentState) -> AgentState:
        """Generate comprehensive answer using Groq"""
        query = state["query"]
        query_type = state["query_type"]
        rag_response = state["rag_response"]
        web_results = state["web_search_results"]
        strategy = state["search_strategy"]
        
        try:
            print(f"🧠 Generating answer with Groq...")
            
            # Prepare internal knowledge
            internal_answer = rag_response.get("answer", "") if rag_response else ""
            
            # Format sources
            internal_sources = ""
            if rag_response and rag_response.get("source_documents"):
                internal_sources = "\n\n📚 INTERNAL SOURCES:\n"
                for i, doc in enumerate(rag_response["source_documents"], 1):
                    category = doc.metadata.get('category', 'Unknown')
                    file_name = doc.metadata.get('file_name', 'Unknown')
                    internal_sources += f"{i}. {category} - {file_name}\n"
            
            if strategy == "RAG + Web Search" and web_results and web_results[0]:
                # Combined answer with web search
                synthesis_prompt = f"""
                You are a research analyst for Zeron, a cybersecurity company. Create a comprehensive response that combines internal knowledge with external research.

                Query: {query}

                Zeron's Internal Knowledge:
                {internal_answer}

                External Research:
                {web_results[0]}

                Instructions:
                1. Start with Zeron's perspective and capabilities
                2. Integrate external research to provide broader context
                3. Use clear sections and professional formatting
                4. Be specific and actionable
                5. Maintain expert, confident tone

                Create a detailed response that showcases Zeron's expertise while providing comprehensive market intelligence.
                """
            else:
                # RAG-only answer
                synthesis_prompt = f"""
                Based on Zeron's internal documentation, provide a comprehensive answer to: {query}

                Internal Knowledge:
                {internal_answer}

                Please enhance this answer by:
                1. Making it well-structured with clear headers
                2. Adding relevant context about Zeron's market position
                3. Including technical details and best practices
                4. Ensuring professional presentation

                Provide a polished, comprehensive response.
                """
            
            # Generate final answer using Groq
            response = self.llm.invoke(synthesis_prompt)
            state["final_answer"] = response.content
            
            # Add source information
            state["final_answer"] += internal_sources
            
            print(f"✅ Answer generated successfully")
            
        except Exception as e:
            print(f"❌ Synthesis error: {e}")
            # Fallback to basic RAG response
            fallback_answer = internal_answer if internal_answer else f"Error: {str(e)}"
            state["final_answer"] = f"{fallback_answer}\n\n⚠️ Note: Enhanced processing unavailable"
        
        return state
    
    def setup_workflow(self):
        """Set up the LangGraph workflow"""
        workflow = StateGraph(AgentState)
        
        # Add nodes for each step
        workflow.add_node("classify", self.classify_query)
        workflow.add_node("rag_search", self.retrieve_from_rag)
        workflow.add_node("web_search", self.perform_web_search)
        workflow.add_node("synthesize", self.synthesize_answer)
        
        # Define the workflow path
        workflow.set_entry_point("classify")
        workflow.add_edge("classify", "rag_search")
        workflow.add_edge("rag_search", "web_search")
        workflow.add_edge("web_search", "synthesize")
        workflow.add_edge("synthesize", END)
        
        self.workflow = workflow.compile()
    
    def research(self, question: str) -> Dict[str, Any]:
        """
        Main research method - processes queries through the complete workflow
        """
        try:
            print(f"\n🔬 ZERON RESEARCH AGENT")
            print(f"Query: '{question}'")
            print("=" * 80)
            
            # Initialize workflow state
            initial_state = {
                "query": question,
                "query_type": "general",
                "rag_context": "",
                "rag_response": {},
                "web_search_results": [],
                "final_answer": "",
                "requires_web_search": False,
                "search_strategy": "RAG Only",
                "confidence_level": "medium"
            }
            
            # Execute the workflow
            result = self.workflow.invoke(initial_state)
            
            return {
                "query": question,
                "answer": result["final_answer"],
                "search_strategy": result["search_strategy"],
                "query_type": result["query_type"],
                "confidence": result["confidence_level"],
                "used_web_search": result["requires_web_search"],
                "rag_sources": len(result["rag_response"].get("source_documents", [])),
                "web_search_performed": len(result["web_search_results"]) > 0,
                "rag_response": result["rag_response"]
            }
            
        except Exception as e:
            print(f"❌ Research workflow error: {e}")
            return {
                "query": question,
                "answer": f"I encountered an error while researching your query: {str(e)}",
                "search_strategy": "Error",
                "query_type": "error",
                "confidence": "low",
                "used_web_search": False,
                "rag_sources": 0,
                "web_search_performed": False,
                "rag_response": {}
            }
    
    def interactive_mode(self):
        """Interactive research interface"""
        print("\n" + "="*80)
        print("🔬 ZERON ENHANCED RESEARCH AGENT")
        print("Groq LLM + Anthropic Web Search | Built on existing ZeronRAG")
        print("="*80)
        
        print("\n📝 EXAMPLE QUERIES:")
        print("\n🏠 Internal Knowledge (RAG Only):")
        print("  • 'Explain compliance management features'")
        print("  • 'How does vendor management work?'")
        print("  • 'Integration guide for attack surface management'")
        
        print("\n🌐 Enhanced Research (RAG + Web Search):")
        print("  • 'Create battle cards: Zeron vs ServiceNow GRC'")
        print("  • 'Who are the top 5 competitors in compliance management?'")
        print("  • 'Latest trends in cybersecurity risk management 2024'")
        print("  • 'Compare Zeron's attack surface management with Rapid7'")
        
        print("\nType 'quit', 'exit', or 'q' to stop")
        print("-" * 80)
        
        while True:
            try:
                question = input("\n💬 Your research query: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q', 'bye']:
                    print("👋 Research session ended!")
                    break
                
                if not question:
                    print("Please enter a valid question")
                    continue
                
                # Process the research query
                result = self.research(question)
                
                # Display result inline
                print(f"\n{'='*80}")
                print(f"🔍 QUERY: {result['query']}")
                print(f"\n🤖 RESEARCH RESULT:\n{result['answer']}")
                print(f"\n📊 METADATA: {result['search_strategy']} | Type: {result['query_type']} | Confidence: {result['confidence']} | Sources: {result['rag_sources']} | Web: {'Yes' if result['web_search_performed'] else 'No'}")
                print("="*80)
                
            except KeyboardInterrupt:
                print("\n👋 Research session ended!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

def main():
    """Main function with environment validation"""
    # Validate required environment variables
    required_vars = [
        "PINECONE_API_KEY", 
        "OPENAI_API_KEY", 
        "GROQ_API_KEY",
        "ANTHROPIC_API_KEY"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {missing_vars}")
        print("\nPlease add to your .env file:")
        for var in missing_vars:
            print(f"  {var}=your_api_key_here")
        return
    
    try:
        # Initialize the enhanced research agent
        agent = ZeronEnhancedRAG()
        
        # Check for command line arguments
        import sys
        if len(sys.argv) > 1:
            # Single query mode
            question = " ".join(sys.argv[1:])
            result = agent.research(question)
            # Display result inline
            print(f"\n{'='*80}")
            print(f"🔍 QUERY: {result['query']}")
            print(f"\n🤖 RESEARCH RESULT:\n{result['answer']}")
            print(f"\n📊 METADATA: {result['search_strategy']} | Type: {result['query_type']} | Confidence: {result['confidence']} | Sources: {result['rag_sources']} | Web: {'Yes' if result['web_search_performed'] else 'No'}")
            print("="*80)
        else:
            # Interactive mode
            agent.interactive_mode()
            
    except Exception as e:
        print(f"❌ Failed to start research agent: {e}")

if __name__ == "__main__":
    main()