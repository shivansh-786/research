#!/usr/bin/env python3
"""
Document Ingestion Pipeline
Chunks documents from docs folder and stores them in Pinecone vector database using LangChain
"""

import os
import json
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

# Environment variables
from dotenv import load_dotenv
load_dotenv()

# LangChain imports
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Pinecone
from pinecone import Pinecone, ServerlessSpec

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentIngestionPipeline:
    """
    Document ingestion pipeline that processes markdown documents,
    chunks them using LangChain, and stores in Pinecone vector database
    """
    
    def __init__(
        self,
        docs_directory: str = "docs",
        pinecone_index_name: str = "zeron-docs",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        environment: str = "gcp-starter"
    ):
        self.docs_directory = Path(docs_directory)
        self.pinecone_index_name = pinecone_index_name
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.environment = environment
        
        # Initialize Pinecone
        self.pc = None
        self.index = None
        self.vector_store = None
        
        # Initialize embeddings
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Text splitters
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Markdown header splitter for better semantic chunking
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
            ]
        )
        
    async def setup_pinecone(self):
        """Initialize Pinecone connection and create index if needed"""
        try:
            # Initialize Pinecone
            self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
            
            # Check if index exists, create if not
            if self.pinecone_index_name not in self.pc.list_indexes().names():
                logger.info(f"Creating Pinecone index: {self.pinecone_index_name}")
                self.pc.create_index(
                    name=self.pinecone_index_name,
                    dimension=1536,  # OpenAI embedding dimension
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"
                    )
                )
                logger.info("Index created successfully")
            else:
                logger.info(f"Using existing Pinecone index: {self.pinecone_index_name}")
            
            # Get index
            self.index = self.pc.Index(self.pinecone_index_name)
            
            # Initialize vector store
            self.vector_store = PineconeVectorStore(
                index=self.index,
                embedding=self.embeddings,
                text_key="text"
            )
            
            logger.info("Pinecone setup completed")
            
        except Exception as e:
            logger.error(f"Error setting up Pinecone: {e}")
            raise
    
    def load_documents(self) -> List[Document]:
        """Load all markdown documents from the docs directory"""
        try:
            logger.info(f"Loading documents from: {self.docs_directory}")
            
            # Load all markdown files
            loader = DirectoryLoader(
                str(self.docs_directory),
                glob="**/*.md",
                loader_cls=TextLoader,
                loader_kwargs={"encoding": "utf-8"}
            )
            
            documents = loader.load()
            logger.info(f"Loaded {len(documents)} documents")
            
            # Add metadata to documents
            for doc in documents:
                # Extract category from file path
                relative_path = Path(doc.metadata["source"]).relative_to(self.docs_directory)
                category = relative_path.parts[0] if len(relative_path.parts) > 1 else "general"
                
                doc.metadata.update({
                    "category": category,
                    "file_name": Path(doc.metadata["source"]).name,
                    "ingestion_timestamp": datetime.now().isoformat(),
                    "relative_path": str(relative_path)
                })
            
            return documents
            
        except Exception as e:
            logger.error(f"Error loading documents: {e}")
            raise
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """Chunk documents using both markdown-aware and recursive splitters"""
        try:
            logger.info("Starting document chunking...")
            all_chunks = []
            
            for doc in documents:
                # First, try markdown header splitting for better semantic chunks
                try:
                    md_header_splits = self.markdown_splitter.split_text(doc.page_content)
                    
                    # If we get meaningful splits, use them
                    if len(md_header_splits) > 1:
                        for i, split_doc in enumerate(md_header_splits):
                            # Further split large chunks
                            if len(split_doc.page_content) > self.chunk_size:
                                sub_chunks = self.text_splitter.split_documents([split_doc])
                                for j, chunk in enumerate(sub_chunks):
                                    chunk.metadata.update(doc.metadata)
                                    chunk.metadata.update({
                                        "chunk_id": f"{doc.metadata['file_name']}_md_{i}_{j}",
                                        "chunk_type": "markdown_header_split",
                                        "parent_chunk": i
                                    })
                                    all_chunks.append(chunk)
                            else:
                                split_doc.metadata.update(doc.metadata)
                                split_doc.metadata.update({
                                    "chunk_id": f"{doc.metadata['file_name']}_md_{i}",
                                    "chunk_type": "markdown_header_split",
                                    "parent_chunk": i
                                })
                                all_chunks.append(split_doc)
                    else:
                        # Fallback to recursive splitting
                        chunks = self.text_splitter.split_documents([doc])
                        for i, chunk in enumerate(chunks):
                            chunk.metadata.update({
                                "chunk_id": f"{doc.metadata['file_name']}_rec_{i}",
                                "chunk_type": "recursive_split"
                            })
                            all_chunks.append(chunk)
                            
                except Exception as e:
                    logger.warning(f"Markdown splitting failed for {doc.metadata['file_name']}: {e}")
                    # Fallback to recursive splitting
                    chunks = self.text_splitter.split_documents([doc])
                    for i, chunk in enumerate(chunks):
                        chunk.metadata.update({
                            "chunk_id": f"{doc.metadata['file_name']}_rec_{i}",
                            "chunk_type": "recursive_split"
                        })
                        all_chunks.append(chunk)
            
            logger.info(f"Created {len(all_chunks)} chunks from {len(documents)} documents")
            return all_chunks
            
        except Exception as e:
            logger.error(f"Error chunking documents: {e}")
            raise
    
    def filter_chunks(self, chunks: List[Document]) -> List[Document]:
        """Filter out very small or empty chunks"""
        filtered_chunks = []
        
        for chunk in chunks:
            # Skip chunks that are too small or mostly whitespace
            if len(chunk.page_content.strip()) < 50:
                continue
                
            # Skip chunks that are just navigation links
            if chunk.page_content.strip().count('[') > 5 and len(chunk.page_content.strip()) < 200:
                continue
                
            # Clean up the content
            chunk.page_content = chunk.page_content.strip()
            filtered_chunks.append(chunk)
        
        logger.info(f"Filtered to {len(filtered_chunks)} chunks from {len(chunks)} original chunks")
        return filtered_chunks
    
    async def store_in_pinecone(self, chunks: List[Document], batch_size: int = 100):
        """Store chunks in Pinecone vector database"""
        try:
            logger.info(f"Storing {len(chunks)} chunks in Pinecone...")
            
            # Process in batches to avoid API limits
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                batch_num = i // batch_size + 1
                total_batches = (len(chunks) + batch_size - 1) // batch_size
                
                logger.info(f"Processing batch {batch_num}/{total_batches} ({len(batch)} chunks)")
                
                try:
                    # Add to vector store
                    self.vector_store.add_documents(batch)
                    logger.info(f"Successfully stored batch {batch_num}")
                    
                    # Small delay to respect rate limits
                    await asyncio.sleep(1)
                    
                except Exception as e:
                    logger.error(f"Error storing batch {batch_num}: {e}")
                    # Continue with next batch
                    continue
            
            logger.info("Document storage completed")
            
        except Exception as e:
            logger.error(f"Error storing in Pinecone: {e}")
            raise
    
    def save_chunk_metadata(self, chunks: List[Document], output_file: str = "chunk_metadata.json"):
        """Save chunk metadata for debugging and analysis"""
        try:
            metadata_list = []
            for chunk in chunks:
                metadata_list.append({
                    "chunk_id": chunk.metadata.get("chunk_id"),
                    "source": chunk.metadata.get("source"),
                    "category": chunk.metadata.get("category"),
                    "file_name": chunk.metadata.get("file_name"),
                    "chunk_type": chunk.metadata.get("chunk_type"),
                    "content_length": len(chunk.page_content),
                    "content_preview": chunk.page_content[:200] + "..." if len(chunk.page_content) > 200 else chunk.page_content
                })
            
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(metadata_list, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Chunk metadata saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error saving chunk metadata: {e}")
    
    async def run_ingestion(self):
        """Main method to run the complete ingestion pipeline"""
        try:
            logger.info("Starting document ingestion pipeline...")
            
            # Step 1: Setup Pinecone
            await self.setup_pinecone()
            
            # Step 2: Load documents
            documents = self.load_documents()
            if not documents:
                logger.warning("No documents found to process")
                return
            
            # Step 3: Chunk documents
            chunks = self.chunk_documents(documents)
            
            # Step 4: Filter chunks
            filtered_chunks = self.filter_chunks(chunks)
            
            # Step 5: Save metadata for analysis
            self.save_chunk_metadata(filtered_chunks)
            
            # Step 6: Store in Pinecone
            await self.store_in_pinecone(filtered_chunks)
            
            # Summary
            logger.info("="*50)
            logger.info("INGESTION PIPELINE COMPLETED")
            logger.info(f"Documents processed: {len(documents)}")
            logger.info(f"Chunks created: {len(chunks)}")
            logger.info(f"Chunks after filtering: {len(filtered_chunks)}")
            logger.info(f"Pinecone index: {self.pinecone_index_name}")
            logger.info("="*50)
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise

# Utility functions
async def test_search(pipeline: DocumentIngestionPipeline, query: str, k: int = 5):
    """Test the vector search functionality"""
    try:
        logger.info(f"Testing search with query: '{query}'")
        
        results = pipeline.vector_store.similarity_search(query, k=k)
        
        print(f"\nSearch Results for: '{query}'")
        print("="*50)
        
        for i, result in enumerate(results, 1):
            print(f"\n{i}. Category: {result.metadata.get('category', 'N/A')}")
            print(f"   File: {result.metadata.get('file_name', 'N/A')}")
            print(f"   Chunk ID: {result.metadata.get('chunk_id', 'N/A')}")
            print(f"   Content: {result.page_content[:300]}...")
            print("-" * 30)
        
    except Exception as e:
        logger.error(f"Error testing search: {e}")

async def main():
    """Main function to run the ingestion pipeline"""
    try:
        # Check environment variables
        required_env_vars = ["OPENAI_API_KEY", "PINECONE_API_KEY"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        
        if missing_vars:
            logger.error(f"Missing required environment variables: {missing_vars}")
            logger.error("Please set them in a .env file or as environment variables")
            return
        
        # Initialize pipeline
        pipeline = DocumentIngestionPipeline(
            docs_directory="docs",
            pinecone_index_name="zeron-docs",
            chunk_size=1000,
            chunk_overlap=200
        )
        
        # Run ingestion
        await pipeline.run_ingestion()
        
        # Test search functionality
        await test_search(pipeline, "compliance audit requirements")
        await test_search(pipeline, "attack surface management dashboard")
        
    except Exception as e:
        logger.error(f"Main execution failed: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 