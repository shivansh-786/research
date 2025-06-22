#!/usr/bin/env python3
"""
Crawl4AI Sitemap Scraper
Scrapes all content from a sitemap URL using Crawl4AI
"""

import asyncio
import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import aiohttp
import aiofiles

# First, install required packages:
# pip install "crawl4ai @ git+https://github.com/unclecode/crawl4ai.git"
# pip install aiohttp aiofiles

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

class SitemapCrawler:
    def __init__(self, sitemap_url: str, output_dir: str = "crawled_content"):
        self.sitemap_url = sitemap_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Create subdirectories
        (self.output_dir / "markdown").mkdir(exist_ok=True)
        (self.output_dir / "html").mkdir(exist_ok=True)
        (self.output_dir / "json").mkdir(exist_ok=True)
        
    async def fetch_sitemap_urls(self) -> List[str]:
        """Fetch and parse sitemap XML to extract all URLs"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.sitemap_url) as response:
                    if response.status == 200:
                        content = await response.text()
                        root = ET.fromstring(content)
                        
                        # Handle XML namespaces
                        namespaces = {
                            'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'
                        }
                        
                        urls = []
                        # Try with namespace first
                        url_elements = root.findall('.//sitemap:url/sitemap:loc', namespaces)
                        if not url_elements:
                            # Fallback without namespace
                            url_elements = root.findall('.//url/loc')
                        
                        for url_elem in url_elements:
                            if url_elem.text:
                                urls.append(url_elem.text.strip())
                        
                        print(f"Found {len(urls)} URLs in sitemap")
                        return urls
                    else:
                        print(f"Failed to fetch sitemap: HTTP {response.status}")
                        return []
        except Exception as e:
            print(f"Error fetching sitemap: {e}")
            return []
    
    async def crawl_single_page(self, crawler, url: str, semaphore: asyncio.Semaphore) -> Dict[str, Any]:
        """Crawl a single page and return the result"""
        async with semaphore:  # Limit concurrent requests
            try:
                print(f"Crawling: {url}")
                
                # Simplified configuration - remove problematic extraction_strategy
                config = CrawlerRunConfig(
                    word_count_threshold=10,
                    bypass_cache=False,
                    process_iframes=True,
                    remove_overlay_elements=True,
                    simulate_user=True,
                    override_navigator=True,
                )
                
                result = await crawler.arun(url=url, config=config)
                
                if result.success:
                    return {
                        "url": url,
                        "title": result.metadata.get("title", ""),
                        "description": result.metadata.get("description", ""),
                        "keywords": result.metadata.get("keywords", ""),
                        "markdown": result.markdown,
                        "cleaned_html": result.cleaned_html,
                        "links": result.links,
                        "media": result.media,
                        "metadata": result.metadata,
                        "status": "success",
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    return {
                        "url": url,
                        "status": "failed",
                        "error": result.error_message,
                        "timestamp": datetime.now().isoformat()
                    }
            except Exception as e:
                return {
                    "url": url,
                    "status": "error",
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                }
    
    async def save_content(self, content_data: Dict[str, Any]):
        """Save crawled content to files"""
        if content_data["status"] != "success":
            return
            
        # Create safe filename from URL
        safe_filename = content_data["url"].replace("https://", "").replace("http://", "")
        safe_filename = "".join(c for c in safe_filename if c.isalnum() or c in ".-_").rstrip(".")
        
        # Save markdown
        if content_data.get("markdown"):
            markdown_file = self.output_dir / "markdown" / f"{safe_filename}.md"
            async with aiofiles.open(markdown_file, 'w', encoding='utf-8') as f:
                await f.write(f"# {content_data.get('title', 'No Title')}\n\n")
                await f.write(f"**URL:** {content_data['url']}\n\n")
                await f.write(f"**Description:** {content_data.get('description', 'N/A')}\n\n")
                await f.write("---\n\n")
                await f.write(content_data["markdown"])
        
        # Save cleaned HTML
        if content_data.get("cleaned_html"):
            html_file = self.output_dir / "html" / f"{safe_filename}.html"
            async with aiofiles.open(html_file, 'w', encoding='utf-8') as f:
                await f.write(content_data["cleaned_html"])
        
        # Save JSON metadata
        json_file = self.output_dir / "json" / f"{safe_filename}.json"
        # Remove large content fields for JSON to keep it manageable
        json_data = {k: v for k, v in content_data.items() 
                    if k not in ["markdown", "cleaned_html"]}
        async with aiofiles.open(json_file, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    
    async def crawl_all_pages(self, max_concurrent: int = 5):
        """Main method to crawl all pages from the sitemap"""
        print(f"Starting sitemap crawl for: {self.sitemap_url}")
        
        # Fetch URLs from sitemap
        urls = await self.fetch_sitemap_urls()
        if not urls:
            print("No URLs found in sitemap")
            return
        
        # Set up browser configuration
        browser_config = BrowserConfig(
            headless=True,
            browser_type="chromium",
            viewport_width=1920,
            viewport_height=1080,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        )
        
        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(max_concurrent)
        
        # Initialize crawler
        async with AsyncWebCrawler(config=browser_config) as crawler:
            print(f"Crawling {len(urls)} pages with max {max_concurrent} concurrent requests...")
            
            # Create tasks for all URLs
            tasks = [
                self.crawl_single_page(crawler, url, semaphore) 
                for url in urls
            ]
            
            # Process all pages
            results = []
            completed = 0
            
            for coro in asyncio.as_completed(tasks):
                try:
                    result = await coro
                    results.append(result)
                    completed += 1
                    
                    # Save content immediately
                    await self.save_content(result)
                    
                    # Progress update
                    status = result["status"]
                    url = result["url"]
                    print(f"[{completed}/{len(urls)}] {status.upper()}: {url}")
                    
                except Exception as e:
                    print(f"Task failed: {e}")
                    completed += 1
            
            # Save summary report
            await self.save_summary_report(results)
            
            print(f"\nCrawling completed!")
            print(f"Total pages: {len(results)}")
            print(f"Successful: {len([r for r in results if r['status'] == 'success'])}")
            print(f"Failed: {len([r for r in results if r['status'] != 'success'])}")
            print(f"Output directory: {self.output_dir.absolute()}")
    
    async def save_summary_report(self, results: List[Dict[str, Any]]):
        """Save a summary report of the crawling session"""
        successful = [r for r in results if r["status"] == "success"]
        failed = [r for r in results if r["status"] != "success"]
        
        report = {
            "sitemap_url": self.sitemap_url,
            "crawl_timestamp": datetime.now().isoformat(),
            "total_pages": len(results),
            "successful_pages": len(successful),
            "failed_pages": len(failed),
            "success_rate": len(successful) / len(results) * 100 if results else 0,
            "successful_urls": [r["url"] for r in successful],
            "failed_urls": [{"url": r["url"], "error": r.get("error", "Unknown")} for r in failed]
        }
        
        report_file = self.output_dir / "crawl_report.json"
        async with aiofiles.open(report_file, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(report, indent=2, ensure_ascii=False))
        
        print(f"Summary report saved to: {report_file}")

async def main():
    """Main function to run the sitemap crawler"""
    sitemap_url = "https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/sitemap-pages.xml"
    
    # You can customize these settings
    output_directory = "zeron_docs_crawled"
    max_concurrent_requests = 3  # Be respectful to the server
    
    crawler = SitemapCrawler(sitemap_url, output_directory)
    await crawler.crawl_all_pages(max_concurrent_requests)

if __name__ == "__main__":
    # Run the crawler
    asyncio.run(main())