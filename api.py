import os
import uvicorn
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime
import logging
from research_agent import ZeronEnhancedRAG

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Zeron Enhanced Research API",
    description="AI-powered research agent with RAG and web search capabilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ResearchRequest(BaseModel):
    query: str = Field(..., description="Research query to process", min_length=1, max_length=1000)
    include_metadata: bool = Field(default=True, description="Include metadata in response")

class ResearchResponse(BaseModel):
    query: str
    answer: str
    search_strategy: str
    query_type: str
    confidence: str
    used_web_search: bool
    rag_sources: int
    web_search_performed: bool
    timestamp: str
    processing_time_ms: Optional[float] = None

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str
    services: Dict[str, str]

# Global research agent instance
research_agent: Optional[ZeronEnhancedRAG] = None

@app.on_event("startup")
async def startup_event():
    """Initialize the research agent on startup"""
    global research_agent
    try:
        logger.info("🚀 Initializing Zeron Enhanced Research Agent...")
        
        # Validate environment variables
        required_vars = ["PINECONE_API_KEY", "OPENAI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            logger.error(f"❌ Missing required environment variables: {missing_vars}")
            raise Exception(f"Missing environment variables: {missing_vars}")
        
        research_agent = ZeronEnhancedRAG()
        logger.info("✅ Research Agent initialized successfully!")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize research agent: {e}")
        raise e

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with basic API information"""
    return {
        "message": "Zeron Enhanced Research API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    global research_agent
    
    services = {
        "research_agent": "healthy" if research_agent else "not_initialized",
        "groq_llm": "configured" if os.getenv("GROQ_API_KEY") else "not_configured",
        "anthropic": "configured" if os.getenv("ANTHROPIC_API_KEY") else "not_configured",
        "pinecone": "configured" if os.getenv("PINECONE_API_KEY") else "not_configured",
        "openai": "configured" if os.getenv("OPENAI_API_KEY") else "not_configured"
    }
    
    overall_status = "healthy" if all(
        status in ["healthy", "configured"] for status in services.values()
    ) else "degraded"
    
    return HealthResponse(
        status=overall_status,
        timestamp=datetime.now().isoformat(),
        version="1.0.0",
        services=services
    )

@app.post("/research", response_model=ResearchResponse)
async def research_query(request: ResearchRequest):
    """
    Process a research query using the enhanced RAG system
    
    - **query**: The research question to process
    - **include_metadata**: Whether to include detailed metadata in response
    """
    global research_agent
    
    if not research_agent:
        raise HTTPException(
            status_code=503, 
            detail="Research agent not initialized. Check /health endpoint for service status."
        )
    
    try:
        start_time = datetime.now()
        logger.info(f"🔍 Processing research query: {request.query}")
        
        # Process the research query
        result = research_agent.research(request.query)
        
        # Calculate processing time
        processing_time = (datetime.now() - start_time).total_seconds() * 1000
        
        # Prepare response
        response = ResearchResponse(
            query=result["query"],
            answer=result["answer"],
            search_strategy=result["search_strategy"],
            query_type=result["query_type"],
            confidence=result["confidence"],
            used_web_search=result["used_web_search"],
            rag_sources=result["rag_sources"],
            web_search_performed=result["web_search_performed"],
            timestamp=datetime.now().isoformat(),
            processing_time_ms=processing_time if request.include_metadata else None
        )
        
        logger.info(f"✅ Query processed successfully in {processing_time:.2f}ms")
        return response
        
    except Exception as e:
        logger.error(f"❌ Error processing research query: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing research query: {str(e)}"
        )


if __name__ == "__main__":
    # For development - use uvicorn directly in production
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 