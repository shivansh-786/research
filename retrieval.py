#!/usr/bin/env python3
"""
Simple RAG System for Zeron Document Vector Database
Query your Pinecone vector database with natural language questions
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from pinecone import Pinecone as PineconeClient

# Load environment variables
load_dotenv()

class ZeronRAG:
    """Simple RAG system for querying Zeron documents"""
    
    def __init__(self):
        # Configuration - matching your embedding.py setup
        self.index_name = "zeron"  # Your existing Pinecone index
        self.embedding_model = "text-embedding-3-small"
        
        # Initialize clients
        self.pc = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))
        
        # Initialize embeddings (same as embedding.py)
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model=self.embedding_model
        )
        
        # Initialize LLM - using Groq for fast responses
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
            temperature=0.1
        )
        
        # Initialize components
        self.vectorstore = None
        self.qa_chain = None
        
        self.setup_rag_system()
    
    def setup_rag_system(self):
        """Set up the RAG retrieval chain"""
        try:
            print("🔗 Connecting to Pinecone index 'zeron'...")
            
            # Connect to your existing Pinecone index
            self.vectorstore = PineconeVectorStore.from_existing_index(
                index_name=self.index_name,
                embedding=self.embeddings
            )
            
            # Test connection by getting index stats
            index_stats = self.pc.Index(self.index_name).describe_index_stats()
            vector_count = index_stats.get('total_vector_count', 0)
            print(f"✅ Connected! Found {vector_count} vectors in the database")
            
            # Create custom prompt for Zeron documentation
            prompt_template = """You are a helpful AI assistant that answers questions about Zeron's cybersecurity platform based on the provided documentation.

Use the following pieces of context from Zeron's documentation to answer the question. If you don't know the answer based on the context provided, just say that you don't know.

Context from Zeron docs:
{context}

Question: {question}

Answer: """

            PROMPT = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            
            # Create retrieval QA chain
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k": 5}  # Retrieve top 5 most relevant chunks
                ),
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=True
            )
            
            print("🚀 RAG system ready! You can now ask questions about Zeron documentation.")
            
        except Exception as e:
            print(f"❌ Error setting up RAG system: {e}")
            raise
    
    def query(self, question: str):
        """Query the Zeron documentation"""
        try:
            if not self.qa_chain:
                print("❌ RAG system not initialized")
                return None
            
            print(f"🔍 Searching for: '{question}'...")
            
            # Get response from the chain
            response = self.qa_chain({"query": question})
            
            return {
                "answer": response["result"],
                "source_documents": response["source_documents"]
            }
            
        except Exception as e:
            print(f"❌ Error querying documents: {e}")
            return None
    
    def format_response(self, response):
        """Format the response with sources"""
        if not response:
            return "❌ No response generated"
        
        # Main answer
        formatted = f"🤖 Answer:\n{response['answer']}\n\n"
        
        # Add sources
        if response['source_documents']:
            formatted += "📚 Sources:\n"
            for i, doc in enumerate(response['source_documents'], 1):
                category = doc.metadata.get('category', 'Unknown')
                file_name = doc.metadata.get('file_name', 'Unknown file')
                content_preview = doc.page_content[:150] + "..." if len(doc.page_content) > 150 else doc.page_content
                
                formatted += f"{i}. Category: {category} | File: {file_name}\n"
                formatted += f"   Preview: {content_preview}\n\n"
        
        return formatted
    
    def interactive_mode(self):
        """Interactive query interface"""
        print("\n" + "="*60)
        print("🔍 ZERON DOCUMENT RAG SYSTEM")
        print("="*60)
        print("Ask questions about:")
        print("• Compliance management")
        print("• Attack surface management") 
        print("• Cyber risk management")
        print("• Vendor management")
        print("• Integration guides")
        print("\nType 'quit' or 'exit' to stop")
        print("-" * 60)
        
        while True:
            try:
                question = input("\n💬 Your question: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                if not question:
                    print("Please enter a valid question")
                    continue
                
                # Get answer
                response = self.query(question)
                
                if response:
                    print("\n" + "="*60)
                    print(self.format_response(response))
                    print("="*60)
                else:
                    print("❌ Sorry, I couldn't generate a response")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

def single_query(question: str):
    """Process a single query and return formatted response"""
    try:
        rag = ZeronRAG()
        response = rag.query(question)
        
        if response:
            print("\n" + "="*60)
            print(rag.format_response(response))
            print("="*60)
        else:
            print("❌ Sorry, I couldn't generate a response")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main function - supports both single query and interactive mode"""
    # Check environment variables
    required_vars = ["PINECONE_API_KEY", "OPENAI_API_KEY", "GROQ_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Missing environment variables: {missing_vars}")
        print("Please set them in your .env file")
        return
    
    print("🚀 Starting Zeron RAG System...")
    
    try:
        # Initialize RAG system
        rag = ZeronRAG()
        
        # Check if user provided a question as argument
        import sys
        if len(sys.argv) > 1:
            # Single query mode
            question = " ".join(sys.argv[1:])
            response = rag.query(question)
            if response:
                print("\n" + "="*60)
                print(rag.format_response(response))
                print("="*60)
        else:
            # Interactive mode
            rag.interactive_mode()
            
    except Exception as e:
        print(f"❌ Failed to start RAG system: {e}")

if __name__ == "__main__":
    main()