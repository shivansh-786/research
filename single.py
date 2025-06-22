#!/usr/bin/env python3
"""
Simple Crawl4AI single page scraper
"""

import asyncio
from crawl4ai import AsyncWebCrawler

async def scrape_page(url):
    async with AsyncWebCrawler(headless=True) as crawler:
        result = await crawler.arun(url)
        
        if result.success:
            print(f"✅ Successfully scraped: {url}")
            print(f"Title: {result.metadata.get('title', 'No title')}")
            print(f"Content length: {len(result.markdown)} characters")
            
            # Save markdown content
            filename = url.split('/')[-1] or 'page'
            with open(f"{filename}.md", "w", encoding="utf-8") as f:
                f.write(f"# {result.metadata.get('title', 'No Title')}\n\n")
                f.write(f"**URL:** {url}\n\n")
                f.write("---\n\n")
                f.write(result.markdown)
            
            print(f"Content saved to: {filename}.md")
            return result.markdown
        else:
            print(f"❌ Failed to scrape: {result.error_message}")
            return None

# Usage
if __name__ == "__main__":
    # Change this URL to whatever you want to scrape
    url = "https://docs.zeron.one/zin-advisor"
    
    # Run the scraper
    content = asyncio.run(scrape_page(url))