"""
Python Web Crawler Package
A comprehensive web crawling solution
"""

try:
    from .python_webcrawler import PythonWebCrawler, Result, parse_headers
    from .webcrawler import UnifiedWebCrawler
except ImportError:
    # Handle relative import issues
    import python_webcrawler
    import webcrawler
    PythonWebCrawler = python_webcrawler.PythonWebCrawler
    Result = python_webcrawler.Result
    parse_headers = python_webcrawler.parse_headers
    UnifiedWebCrawler = webcrawler.UnifiedWebCrawler

__version__ = "1.0.0"
__author__ = "Shubham"

__all__ = [
    "PythonWebCrawler",
    "Result",
    "parse_headers",
    "UnifiedWebCrawler"
]
