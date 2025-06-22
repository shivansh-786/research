#!/usr/bin/env python3
"""
Document Embedding and Pinecone Ingestion
Uses OpenAI embeddings to vectorize chunked documents and stores them in Pinecone vector database
"""

import os
import json
import time
from typing import List, Dict, Any
import logging
from pathlib import Path

# Environment variables
from dotenv import load_dotenv
load_dotenv()

# OpenAI and Pinecone imports
import openai
from pinecone import Pinecone, ServerlessSpec
import tiktoken

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentEmbedder:
    """Embeds documents using OpenAI and stores in Pinecone"""
    
    def __init__(self, pinecone_index_name: str = "zeron", batch_size: int = 100):
        # Configuration
        self.pinecone_index_name = pinecone_index_name
        self.batch_size = batch_size
        self.embedding_model = "text-embedding-3-small"  # Latest OpenAI model
        self.embedding_dimension = 1536
        
        # Initialize clients
        self.openai_client = None
        self.pinecone_client = None
        self.pinecone_index = None
        
        # Token counter for cost estimation
        self.encoding = tiktoken.encoding_for_model("text-embedding-3-small")
        
        # Statistics
        self.stats = {
            "total_chunks": 0,
            "successful_embeddings": 0,
            "failed_embeddings": 0,
            "total_tokens": 0,
            "estimated_cost": 0.0
        }
    
    def setup_clients(self):
        """Initialize OpenAI and Pinecone clients"""
        try:
            # Setup OpenAI
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("OPENAI_API_KEY environment variable not set")
            
            self.openai_client = openai.OpenAI(api_key=openai_api_key)
            logger.info("OpenAI client initialized")
            
            # Setup Pinecone
            pinecone_api_key = os.getenv("PINECONE_API_KEY")
            if not pinecone_api_key:
                raise ValueError("PINECONE_API_KEY environment variable not set")
            
            self.pinecone_client = Pinecone(api_key=pinecone_api_key)
            
            # Connect to existing index
            try:
                self.pinecone_index = self.pinecone_client.Index(self.pinecone_index_name)
                logger.info(f"Connected to Pinecone index: {self.pinecone_index_name}")
                
                # Get index stats
                index_stats = self.pinecone_index.describe_index_stats()
                logger.info(f"Index stats: {index_stats.get('total_vector_count', 0)} vectors")
                
            except Exception as e:
                logger.error(f"Failed to connect to Pinecone index '{self.pinecone_index_name}': {e}")
                logger.info("Make sure the index exists in your Pinecone dashboard")
                raise
                
        except Exception as e:
            logger.error(f"Error setting up clients: {e}")
            raise
    
    def load_chunked_data(self, file_path: str = "result.txt") -> Dict[str, Any]:
        """Load chunked document data from result.txt"""
        try:
            if not Path(file_path).exists():
                raise FileNotFoundError(f"Chunked data file not found: {file_path}")
            
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            logger.info(f"Loaded {data['summary']['total_chunks']} chunks from {file_path}")
            return data
            
        except Exception as e:
            logger.error(f"Error loading chunked data: {e}")
            raise
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in text for cost estimation"""
        return len(self.encoding.encode(text))
    
    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Create embeddings for a batch of texts using OpenAI"""
        try:
            # Count tokens for cost estimation
            total_tokens = sum(self.count_tokens(text) for text in texts)
            self.stats["total_tokens"] += total_tokens
            
            # Create embeddings
            response = self.openai_client.embeddings.create(
                model=self.embedding_model,
                input=texts,
                encoding_format="float"
            )
            
            # Extract embeddings
            embeddings = [data.embedding for data in response.data]
            
            # Update cost estimation (text-embedding-3-small: $0.00002 / 1K tokens)
            batch_cost = (total_tokens / 1000) * 0.00002
            self.stats["estimated_cost"] += batch_cost
            
            logger.info(f"Created {len(embeddings)} embeddings ({total_tokens} tokens, ~${batch_cost:.6f})")
            return embeddings
            
        except Exception as e:
            logger.error(f"Error creating embeddings: {e}")
            raise
    
    def prepare_vectors(self, chunk_data: List[Dict[str, Any]], embeddings: List[List[float]]) -> List[Dict[str, Any]]:
        """Prepare vectors for Pinecone upsert"""
        vectors = []
        
        for chunk, embedding in zip(chunk_data, embeddings):
            vector = {
                "id": chunk["id"],
                "values": embedding,
                "metadata": {
                    # Essential metadata for search
                    "text": chunk["text"][:1000],  # Limit text size in metadata
                    "category": chunk["metadata"]["category"],
                    "file_name": chunk["metadata"]["file_name"],
                    "chunk_type": chunk["metadata"]["chunk_type"],
                    "content_length": chunk["metadata"]["content_length"],
                    "relative_path": chunk["metadata"]["relative_path"]
                }
            }
            vectors.append(vector)
        
        return vectors
    
    def upsert_vectors(self, vectors: List[Dict[str, Any]]):
        """Upload vectors to Pinecone"""
        try:
            # Upsert vectors
            upsert_response = self.pinecone_index.upsert(vectors=vectors)
            
            if upsert_response.get("upserted_count", 0) == len(vectors):
                logger.info(f"Successfully upserted {len(vectors)} vectors")
                self.stats["successful_embeddings"] += len(vectors)
            else:
                logger.warning(f"Partial upsert: {upsert_response.get('upserted_count', 0)}/{len(vectors)} vectors")
                self.stats["successful_embeddings"] += upsert_response.get("upserted_count", 0)
                self.stats["failed_embeddings"] += len(vectors) - upsert_response.get("upserted_count", 0)
            
            # Small delay to respect rate limits
            time.sleep(0.5)
            
        except Exception as e:
            logger.error(f"Error upserting vectors: {e}")
            self.stats["failed_embeddings"] += len(vectors)
            raise
    
    def process_chunks_in_batches(self, chunked_data: Dict[str, Any]):
        """Process chunks in batches for embedding and storage"""
        try:
            chunks = chunked_data["vectors"]
            self.stats["total_chunks"] = len(chunks)
            
            logger.info(f"Processing {len(chunks)} chunks in batches of {self.batch_size}")
            
            for i in range(0, len(chunks), self.batch_size):
                batch = chunks[i:i + self.batch_size]
                batch_num = i // self.batch_size + 1
                total_batches = (len(chunks) + self.batch_size - 1) // self.batch_size
                
                logger.info(f"Processing batch {batch_num}/{total_batches} ({len(batch)} chunks)")
                
                try:
                    # Extract texts for embedding
                    texts = [chunk["text"] for chunk in batch]
                    
                    # Create embeddings
                    embeddings = self.create_embeddings(texts)
                    
                    # Prepare vectors
                    vectors = self.prepare_vectors(batch, embeddings)
                    
                    # Upsert to Pinecone
                    self.upsert_vectors(vectors)
                    
                    logger.info(f"Batch {batch_num} completed successfully")
                    
                except Exception as e:
                    logger.error(f"Error processing batch {batch_num}: {e}")
                    # Continue with next batch
                    continue
            
            logger.info("All batches processed")
            
        except Exception as e:
            logger.error(f"Error processing chunks: {e}")
            raise
    
    def test_search(self, query: str = "compliance audit requirements", top_k: int = 3):
        """Test the embedded vectors with a search query"""
        try:
            logger.info(f"Testing search with query: '{query}'")
            
            # Create embedding for query
            query_embedding = self.create_embeddings([query])[0]
            
            # Search in Pinecone
            search_results = self.pinecone_index.query(
                vector=query_embedding,
                top_k=top_k,
                include_values=False,
                include_metadata=True
            )
            
            print(f"\n🔍 Search Results for: '{query}'")
            print("=" * 60)
            
            for i, match in enumerate(search_results.matches, 1):
                print(f"\n{i}. Score: {match.score:.4f}")
                print(f"   Category: {match.metadata.get('category', 'N/A')}")
                print(f"   File: {match.metadata.get('file_name', 'N/A')}")
                print(f"   Type: {match.metadata.get('chunk_type', 'N/A')}")
                print(f"   Content: {match.metadata.get('text', 'N/A')[:200]}...")
                print("-" * 40)
            
        except Exception as e:
            logger.error(f"Error testing search: {e}")
    
    def print_summary(self):
        """Print processing summary"""
        print("\n" + "=" * 60)
        print("🚀 EMBEDDING & INGESTION COMPLETED")
        print("=" * 60)
        print(f"📊 Total chunks processed: {self.stats['total_chunks']}")
        print(f"✅ Successful embeddings: {self.stats['successful_embeddings']}")
        print(f"❌ Failed embeddings: {self.stats['failed_embeddings']}")
        print(f"🔤 Total tokens used: {self.stats['total_tokens']:,}")
        print(f"💰 Estimated cost: ${self.stats['estimated_cost']:.6f}")
        print(f"📋 Pinecone index: {self.pinecone_index_name}")
        print("=" * 60)
    
    def run_embedding_pipeline(self, chunked_data_file: str = "result.txt"):
        """Main method to run the complete embedding pipeline"""
        try:
            logger.info("Starting embedding and ingestion pipeline...")
            
            # Setup clients
            self.setup_clients()
            
            # Load chunked data
            chunked_data = self.load_chunked_data(chunked_data_file)
            
            # Process chunks in batches
            self.process_chunks_in_batches(chunked_data)
            
            # Print summary
            self.print_summary()
            
            # Test search functionality
            self.test_search("compliance audit requirements")
            self.test_search("attack surface management dashboard")
            
            logger.info("Pipeline completed successfully!")
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            self.print_summary()
            raise

def main():
    """Main function"""
    try:
        # Check environment variables
        required_env_vars = ["OPENAI_API_KEY", "PINECONE_API_KEY"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {missing_vars}")
            print("Please set them in a .env file or as environment variables")
            return
        
        # Check if chunked data exists
        if not Path("result.txt").exists():
            print("❌ result.txt not found. Please run chunking.py first to generate chunked data.")
            return
        
        # Initialize embedder
        embedder = DocumentEmbedder(
            pinecone_index_name="zeron",  # Your existing index name
            batch_size=50  # Adjust based on rate limits
        )
        
        # Run pipeline
        embedder.run_embedding_pipeline()
        
    except Exception as e:
        logger.error(f"Main execution failed: {e}")

if __name__ == "__main__":
    main() 