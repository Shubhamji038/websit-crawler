#!/usr/bin/env python3
"""
GUI usage examples for Python Web Crawler
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from webcrawler import UnifiedWebCrawler


def demo_gui_features():
    """Demonstrate GUI features programmatically"""
    print("🕷️ GUI Features Demo")
    print("=" * 40)
    
    crawler = UnifiedWebCrawler()
    
    # Demo option parsing
    print("\n📝 Option Parsing Examples:")
    test_cases = ["2a", "2b3", "3c2", "1", "invalid"]
    
    for case in test_cases:
        main, export, depth = crawler.parse_option(case)
        print(f"Input: '{case}' -> Main: {main}, Export: {export}, Depth: {depth}")
    
    # Demo result formatting (simulated)
    print("\n📊 Result Formatting:")
    
    # Simulate some results
    from python_webcrawler import Result
    crawler.last_results = [
        Result("https://example.com/page1", "href", "https://example.com"),
        Result("https://example.com/script.js", "script", "https://example.com/page1"),
        Result("https://example.com/api", "form", "https://example.com")
    ]
    
    print(f"Simulated {len(crawler.last_results)} results:")
    for i, result in enumerate(crawler.last_results, 1):
        print(f"{i}. [{result.source}] {result.url}")
    
    # Demo export functionality
    print("\n💾 Export Demo:")
    filename = "demo_export"
    
    try:
        crawler.export_results(filename, "txt")
        crawler.export_results(filename, "json") 
        crawler.export_results(filename, "csv")
        print("✅ All export formats created successfully")
    except Exception as e:
        print(f"❌ Export error: {e}")


def show_gui_structure():
    """Show the GUI structure and features"""
    print("\n🏗️ GUI Structure Overview:")
    print("-" * 30)
    
    features = {
        "Instant Scan": "One-click scanning with auto-export",
        "Quick Scan": "Basic options with format choice", 
        "Advanced Scan": "Full parameter control",
        "Batch Scan": "Multiple URL processing",
        "Export Options": "TXT, JSON, CSV formats",
        "Combined Options": "Smart parsing (e.g., '2a3')"
    }
    
    for feature, description in features.items():
        print(f"• {feature}: {description}")


def show_usage_examples():
    """Show practical usage examples"""
    print("\n📚 Usage Examples:")
    print("-" * 30)
    
    examples = [
        ("Instant Scan", "Double-click RUN.bat → Option 1 → Enter URL"),
        ("Quick Scan + JSON", "Option 2b → Enter URL → Choose depth"),
        ("Advanced + CSV + Depth 3", "Option 3c3 → Configure all settings"),
        ("Batch Processing", "Option 4 → Enter multiple URLs"),
        ("Export Previous Results", "Option 5 → Choose format")
    ]
    
    for example, description in examples:
        print(f"• {example}: {description}")


def main():
    """Run GUI demo"""
    print("🎮 Python Web Crawler GUI Demo")
    print("=" * 40)
    
    try:
        demo_gui_features()
        show_gui_structure()
        show_usage_examples()
        
        print("\n✅ GUI demo completed!")
        print("\nTo run the actual GUI:")
        print("1. Double-click RUN.bat")
        print("2. Or run: python src/webcrawler.py")
        
    except Exception as e:
        print(f"❌ Error in demo: {e}")


if __name__ == "__main__":
    main()
