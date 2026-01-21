#!/usr/bin/env python3
"""
Test suite for Python Web Crawler
"""

import unittest
import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from python_webcrawler import PythonWebCrawler, Result, parse_headers


class TestPythonWebCrawler(unittest.TestCase):
    """Test cases for PythonWebCrawler class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.crawler = PythonWebCrawler(max_depth=1, max_threads=1)
    
    def test_result_creation(self):
        """Test Result class creation and methods"""
        result = Result("https://example.com", "href", "https://source.com")
        self.assertEqual(result.url, "https://example.com")
        self.assertEqual(result.source, "href")
        self.assertEqual(result.where, "https://source.com")
        
        result_dict = result.to_dict()
        expected = {"url": "https://example.com", "source": "href", "where": "https://source.com"}
        self.assertEqual(result_dict, expected)
    
    def test_url_normalization(self):
        """Test URL normalization functionality"""
        # Test relative URL
        normalized = self.crawler._normalize_url("https://example.com/page", "/test")
        self.assertEqual(normalized, "https://example.com/test")
        
        # Test absolute URL
        normalized = self.crawler._normalize_url("https://example.com", "https://other.com")
        self.assertEqual(normalized, "https://other.com")
        
        # Test invalid URLs
        self.assertIsNone(self.crawler._normalize_url("https://example.com", "javascript:void(0)"))
        self.assertIsNone(self.crawler._normalize_url("https://example.com", "mailto:test@example.com"))
        self.assertIsNone(self.crawler._normalize_url("https://example.com", ""))
    
    def test_domain_filtering(self):
        """Test domain filtering logic"""
        # Same domain
        self.assertTrue(self.crawler._is_allowed_domain("https://example.com", "https://example.com/page"))
        
        # Different domain
        self.assertFalse(self.crawler._is_allowed_domain("https://example.com", "https://other.com"))
        
        # Subdomain test
        crawler_with_subs = PythonWebCrawler(subs=True)
        self.assertTrue(crawler_with_subs._is_allowed_domain("https://example.com", "https://sub.example.com"))
    
    def test_path_filtering(self):
        """Test path filtering logic"""
        # Inside path
        crawler_inside = PythonWebCrawler(inside=True)
        self.assertTrue(crawler_inside._is_inside_path("https://example.com/path", "https://example.com/path/page"))
        self.assertFalse(crawler_inside._is_inside_path("https://example.com/path", "https://example.com/other"))
        
        # No path restriction
        crawler_no_inside = PythonWebCrawler(inside=False)
        self.assertTrue(crawler_no_inside._is_inside_path("https://example.com/path", "https://example.com/other"))
    
    def test_parse_headers(self):
        """Test header parsing functionality"""
        headers_str = "User-Agent: Bot/1.0;;Accept: text/html"
        headers = parse_headers(headers_str)
        
        expected = {
            "User-Agent": "Bot/1.0",
            "Accept": "text/html"
        }
        self.assertEqual(headers, expected)
        
        # Test empty string
        self.assertEqual(parse_headers(""), {})
        self.assertEqual(parse_headers(None), {})


class TestUnifiedWebCrawler(unittest.TestCase):
    """Test cases for UnifiedWebCrawler class"""
    
    def setUp(self):
        """Set up test fixtures"""
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
        from webcrawler import UnifiedWebCrawler
        self.crawler = UnifiedWebCrawler()
    
    def test_option_parsing(self):
        """Test combined option parsing"""
        # Test simple option
        main, export, depth = self.crawler.parse_option("2a")
        self.assertEqual(main, 2)
        self.assertEqual(export, "txt")
        self.assertIsNone(depth)
        
        # Test combined option
        main, export, depth = self.crawler.parse_option("2b3")
        self.assertEqual(main, 2)
        self.assertEqual(export, "json")
        self.assertEqual(depth, 3)
        
        # Test invalid option
        main, export, depth = self.crawler.parse_option("invalid")
        self.assertIsNone(main)
        self.assertIsNone(export)
        self.assertIsNone(depth)


if __name__ == '__main__':
    unittest.main()
