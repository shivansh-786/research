#!/usr/bin/env python3
"""
Precise Document Chunking Tool
Chunks markdown documents from /Users/shivanshmahajan/Desktop/zeron/re/docs and saves results to result.txt
"""

import json
from pathlib import Path
from typing import List
import logging

# LangChain imports
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.schema import Document

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentChunker:
    """Precise document chunking with LangChain"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.docs_path = Path("/Users/shivanshmahajan/Desktop/zeron/re/docs")
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Text splitters
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        # Markdown header splitter
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
            ]
        )
    
    def load_documents(self) -> List[Document]:
        """Load all markdown documents"""
        logger.info(f"Loading documents from: {self.docs_path}")
        
        if not self.docs_path.exists():
            raise FileNotFoundError(f"Directory not found: {self.docs_path}")
        
        loader = DirectoryLoader(
            str(self.docs_path),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        
        documents = loader.load()
        logger.info(f"Loaded {len(documents)} documents")
        
        # Add metadata
        for doc in documents:
            relative_path = Path(doc.metadata["source"]).relative_to(self.docs_path)
            category = relative_path.parts[0] if len(relative_path.parts) > 1 else "general"
            
            doc.metadata.update({
                "category": category,
                "file_name": Path(doc.metadata["source"]).name,
                "relative_path": str(relative_path)
            })
        
        return documents
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """Chunk documents using intelligent splitting"""
        logger.info("Chunking documents...")
        all_chunks = []
        
        for doc in documents:
            try:
                # Try markdown header splitting first
                md_splits = self.markdown_splitter.split_text(doc.page_content)
                
                if len(md_splits) > 1:
                    # Use markdown splits
                    for i, split_doc in enumerate(md_splits):
                        if len(split_doc.page_content) > self.chunk_size:
                            # Further split large chunks
                            sub_chunks = self.text_splitter.split_documents([split_doc])
                            for j, chunk in enumerate(sub_chunks):
                                chunk.metadata.update(doc.metadata)
                                chunk.metadata["chunk_id"] = f"{doc.metadata['file_name']}_md_{i}_{j}"
                                chunk.metadata["chunk_type"] = "markdown_header_split"
                                all_chunks.append(chunk)
                        else:
                            split_doc.metadata.update(doc.metadata)
                            split_doc.metadata["chunk_id"] = f"{doc.metadata['file_name']}_md_{i}"
                            split_doc.metadata["chunk_type"] = "markdown_header_split"
                            all_chunks.append(split_doc)
                else:
                    # Fallback to recursive splitting
                    chunks = self.text_splitter.split_documents([doc])
                    for i, chunk in enumerate(chunks):
                        chunk.metadata["chunk_id"] = f"{doc.metadata['file_name']}_rec_{i}"
                        chunk.metadata["chunk_type"] = "recursive_split"
                        all_chunks.append(chunk)
                        
            except Exception as e:
                logger.warning(f"Error processing {doc.metadata['file_name']}: {e}")
                # Fallback to recursive splitting
                chunks = self.text_splitter.split_documents([doc])
                for i, chunk in enumerate(chunks):
                    chunk.metadata["chunk_id"] = f"{doc.metadata['file_name']}_rec_{i}"
                    chunk.metadata["chunk_type"] = "recursive_split"
                    all_chunks.append(chunk)
        
        logger.info(f"Created {len(all_chunks)} chunks from {len(documents)} documents")
        return all_chunks
    
    def filter_chunks(self, chunks: List[Document]) -> List[Document]:
        """Filter out low-quality chunks"""
        filtered = []
        
        for chunk in chunks:
            content = chunk.page_content.strip()
            
            # Skip very small chunks
            if len(content) < 50:
                continue
                
            # Skip chunks that are mostly links
            if content.count('[') > 5 and len(content) < 200:
                continue
                
            chunk.page_content = content
            filtered.append(chunk)
        
        logger.info(f"Filtered to {len(filtered)} chunks from {len(chunks)} original chunks")
        return filtered
    
    def save_results(self, chunks: List[Document]):
        """Save chunking results in Pinecone-compatible format to result.txt"""
        try:
            # Prepare Pinecone-compatible data structure
            pinecone_data = {
                "summary": {
                    "total_chunks": len(chunks),
                    "avg_length": sum(len(chunk.page_content) for chunk in chunks) / len(chunks) if chunks else 0,
                    "categories": {},
                    "chunk_types": {}
                },
                "vectors": []
            }
            
            # Calculate summary statistics
            for chunk in chunks:
                category = chunk.metadata.get("category", "unknown")
                chunk_type = chunk.metadata.get("chunk_type", "unknown")
                pinecone_data["summary"]["categories"][category] = pinecone_data["summary"]["categories"].get(category, 0) + 1
                pinecone_data["summary"]["chunk_types"][chunk_type] = pinecone_data["summary"]["chunk_types"].get(chunk_type, 0) + 1
            
            # Prepare vector data for Pinecone ingestion
            for chunk in chunks:
                vector_data = {
                    "id": chunk.metadata.get("chunk_id", f"chunk_{str(abs(hash(chunk.page_content)))[:8]}"),
                    "text": chunk.page_content,
                    "metadata": {
                        "category": chunk.metadata.get("category", "unknown"),
                        "file_name": chunk.metadata.get("file_name", "unknown"),
                        "chunk_type": chunk.metadata.get("chunk_type", "unknown"),
                        "relative_path": chunk.metadata.get("relative_path", "unknown"),
                        "content_length": len(chunk.page_content),
                        "source": chunk.metadata.get("source", "unknown")
                    }
                }
                pinecone_data["vectors"].append(vector_data)
            
            # Save as JSON format for easy Pinecone integration
            with open("result.txt", "w", encoding="utf-8") as f:
                json.dump(pinecone_data, f, indent=2, ensure_ascii=False)
            
            # Also save a human-readable summary
            with open("result_summary.txt", "w", encoding="utf-8") as f:
                f.write("PINECONE-COMPATIBLE CHUNKING RESULTS\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Total chunks ready for embedding: {len(chunks)}\n")
                f.write(f"Average chunk length: {pinecone_data['summary']['avg_length']:.0f} characters\n\n")
                
                f.write("Categories:\n")
                for category, count in sorted(pinecone_data["summary"]["categories"].items()):
                    f.write(f"  {category}: {count} chunks\n")
                
                f.write(f"\nChunk types:\n")
                for chunk_type, count in sorted(pinecone_data["summary"]["chunk_types"].items()):
                    f.write(f"  {chunk_type}: {count} chunks\n")
                
                f.write(f"\nData structure:\n")
                f.write(f"- Each vector has unique ID, text content, and metadata\n")
                f.write(f"- Compatible with Pinecone vector database\n")
                f.write(f"- Ready for embedding with OpenAI or other models\n")
                f.write(f"- Use result.txt for programmatic access\n")
            
            logger.info("Pinecone-compatible results saved to result.txt")
            logger.info("Human-readable summary saved to result_summary.txt")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            raise
    
    def run(self):
        """Main execution method"""
        try:
            logger.info("Starting document chunking process...")
            
            # Load documents
            documents = self.load_documents()
            if not documents:
                logger.warning("No documents found")
                return
            
            # Chunk documents
            chunks = self.chunk_documents(documents)
            
            # Filter chunks
            filtered_chunks = self.filter_chunks(chunks)
            
            # Save results
            self.save_results(filtered_chunks)
            
            # Print summary
            print("\n" + "=" * 50)
            print("CHUNKING COMPLETED SUCCESSFULLY")
            print("=" * 50)
            print(f"Documents processed: {len(documents)}")
            print(f"Total chunks created: {len(chunks)}")
            print(f"Chunks after filtering: {len(filtered_chunks)}")
            print(f"Results saved to: result.txt")
            print("=" * 50)
            
        except Exception as e:
            logger.error(f"Chunking process failed: {e}")
            raise

def main():
    """Main function"""
    try:
        chunker = DocumentChunker(chunk_size=1000, chunk_overlap=200)
        chunker.run()
    except Exception as e:
        logger.error(f"Execution failed: {e}")

if __name__ == "__main__":
    main() 