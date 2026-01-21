#!/usr/bin/env python3
"""
Basic usage examples for Python Web Crawler
"""

import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from python_webcrawler import PythonWebCrawler


async def basic_crawl_example():
    """Basic crawling example"""
    print("Basic crawling example:")
    print("-" * 30)
    
    crawler = PythonWebCrawler(
        max_depth=2,
        show_source=True,
        unique=True
    )
    
    await crawler.crawl(["https://httpbin.org/"])
    
    print(f"Found {len(crawler.results)} URLs:")
    for i, result in enumerate(crawler.results[:5], 1):
        print(f"{i}. [{result.source}] {result.url}")
    
    if len(crawler.results) > 5:
        print(f"... and {len(crawler.results) - 5} more")


async def advanced_crawl_example():
    """Advanced crawling with custom options"""
    print("\nAdvanced crawling example:")
    print("-" * 30)
    
    crawler = PythonWebCrawler(
        max_depth=3,
        max_threads=4,
        timeout=30,
        max_size=100,  # 100KB limit
        show_source=True,
        show_where=True,
        json_output=False,
        unique=True,
        custom_headers={
            'User-Agent': 'Python WebCrawler/1.0',
            'Accept': 'text/html,application/xhtml+xml'
        }
    )
    
    await crawler.crawl(["https://httpbin.org/"])
    
    print(f"Found {len(crawler.results)} URLs with details:")
    for i, result in enumerate(crawler.results[:3], 1):
        where_info = f" from {result.where}" if result.where else ""
        print(f"{i}. [{result.source}] {result.url}{where_info}")


async def json_output_example():
    """Example with JSON output"""
    print("\nJSON output example:")
    print("-" * 30)
    
    crawler = PythonWebCrawler(
        max_depth=2,
        json_output=True,
        unique=True
    )
    
    await crawler.crawl(["https://httpbin.org/"])
    
    # Get JSON output
    json_output = crawler.format_output()
    print("JSON output (first 500 chars):")
    print(json_output[:500] + "..." if len(json_output) > 500 else json_output)


async def main():
    """Run all examples"""
    print("🕷️ Python Web Crawler Examples")
    print("=" * 40)
    
    try:
        await basic_crawl_example()
        await advanced_crawl_example()
        await json_output_example()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")


if __name__ == "__main__":
    asyncio.run(main())
