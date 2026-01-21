"""
Python Web Crawler Package
A comprehensive web crawling solution
"""

from .python_webcrawler import PythonWebCrawler, Result, parse_headers
from .webcrawler import UnifiedWebCrawler

__version__ = "1.0.0"
__author__ = "Python Web Crawler Team"
__email__ = "contact@example.com"

__all__ = [
    "PythonWebCrawler",
    "Result", 
    "parse_headers",
    "UnifiedWebCrawler"
]
