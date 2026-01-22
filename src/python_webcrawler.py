#!/usr/bin/env python3
"""
Python Web Crawler - A hakrawler-inspired web crawler for gathering URLs
and JavaScript file locations.
"""

import argparse
import asyncio
import json
import sys
from typing import Set, Dict, List, Optional
from urllib.parse import urljoin, urlparse, urlunparse
import ssl

import aiohttp
from bs4 import BeautifulSoup
from aiohttp import ClientTimeout, ClientSession


class Result:
    def __init__(self, url: str, source: str, where: str = ""):
        self.url = url
        self.source = source
        self.where = where

    def to_dict(self):
        return {"url": self.url, "source": self.source, "where": self.where}


class PythonWebCrawler:
    def __init__(
        self,
        max_depth: int = 2,
        max_threads: int = 8,
        max_size: int = -1,
        insecure: bool = False,
        subs: bool = False,
        inside: bool = False,
        show_source: bool = False,
        show_where: bool = False,
        json_output: bool = False,
        unique: bool = False,
        proxy: Optional[str] = None,
        timeout: int = -1,
        disable_redirects: bool = False,
        custom_headers: Optional[Dict[str, str]] = None,
        live_output: bool = False
    ):
        self.max_depth = max_depth
        self.max_threads = max_threads
        self.max_size = max_size * 1024 if max_size > 0 else None
        self.insecure = insecure
        self.subs = subs
        self.inside = inside
        self.show_source = show_source
        self.show_where = show_where
        self.json_output = json_output
        self.unique = unique
        self.proxy = proxy
        self.timeout = timeout
        self.disable_redirects = disable_redirects
        self.custom_headers = custom_headers or {}
        self.live_output = live_output

        self.seen_urls: Set[str] = set()
        self.results: List[Result] = []
        self.session: Optional[ClientSession] = None

        # Default user agent
        self.custom_headers.setdefault(
            'User-Agent',
            'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) '
            'Gecko/20100101 Firefox/78.0'
        )

    def _get_ssl_context(self):
        """Create SSL context based on insecure flag."""
        if self.insecure:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            return ssl_context
        return None

    def _is_allowed_domain(self, base_url: str, target_url: str) -> bool:
        """Check if target URL is in allowed domain."""
        if self.subs:
            # Allow subdomains
            base_domain = urlparse(base_url).netloc
            target_domain = urlparse(target_url).netloc
            return target_domain.endswith(base_domain) or base_domain.endswith(
                target_domain
            )
        else:
            # Only allow same domain
            base_domain = urlparse(base_url).netloc
            target_domain = urlparse(target_url).netloc
            return base_domain == target_domain

    def _is_inside_path(self, base_url: str, target_url: str) -> bool:
        """Check if target URL is inside the base path."""
        if not self.inside:
            return True

        base_path = urlparse(base_url).path
        target_path = urlparse(target_url).path
        return target_path.startswith(base_path)

    def _normalize_url(self, base_url: str, url: str) -> Optional[str]:
        """Normalize and validate URL."""
        if not url or url.startswith(('javascript:', 'mailto:', 'tel:', '#')):
            return None

        # Convert relative URLs to absolute
        if url.startswith('//'):
            url = 'https:' + url
        elif not url.startswith(('http://', 'https://')):
            url = urljoin(base_url, url)

        try:
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                return None
            return urlunparse(parsed)
        except Exception:
            return None

    async def _fetch_page(self, url: str) -> Optional[str]:
        """Fetch page content."""
        try:
            timeout = ClientTimeout(
                total=self.timeout if self.timeout > 0 else None
            )
            _ = aiohttp.TCPConnector(ssl=self._get_ssl_context())

            async with self.session.get(
                url,
                timeout=timeout,
                allow_redirects=not self.disable_redirects,
                headers=self.custom_headers
            ) as response:
                if response.status == 200:
                    content = await response.text()
                    if self.max_size and len(content) > self.max_size:
                        return None
                    return content
        except Exception as e:
            print(f"[error] Failed to fetch {url}: {e}", file=sys.stderr)
        return None

    def _extract_links(self, html: str, base_url: str) -> List[tuple]:
        """Extract links from HTML content."""
        soup = BeautifulSoup(html, 'html.parser')
        links = []

        # Extract href links
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            normalized = self._normalize_url(base_url, href)
            if normalized:
                links.append((normalized, 'href'))

        # Extract script sources
        for script_tag in soup.find_all('script', src=True):
            src = script_tag['src']
            normalized = self._normalize_url(base_url, src)
            if normalized:
                links.append((normalized, 'script'))

        # Extract form actions
        for form_tag in soup.find_all('form', action=True):
            action = form_tag['action']
            normalized = self._normalize_url(base_url, action)
            if normalized:
                links.append((normalized, 'form'))

        return links

    async def _crawl_url(self, url: str, depth: int, source_url: str = ""):
        """Crawl a single URL."""
        if depth > self.max_depth or url in self.seen_urls:
            return

        if self.unique and url in self.seen_urls:
            return

        self.seen_urls.add(url)

        content = await self._fetch_page(url)
        if not content:
            return

        links = self._extract_links(content, url)

        for link_url, source_type in links:
            # Check if we should follow this link
            if self._is_allowed_domain(url, link_url) and self._is_inside_path(
                url, link_url
            ):
                # Add result
                result = Result(
                    url=link_url,
                    source=source_type,
                    where=source_url if self.show_where else ""
                )
                self.results.append(result)
                
                # Live output if enabled
                if self.live_output:
                    line = result.url
                    if self.show_source:
                        line = f"[{result.source}] {line}"
                    if self.show_where and result.where:
                        line = f"[{result.where}] {line}"
                    print(line)

                # Follow link if it's an href and within depth
                if source_type == 'href' and depth < self.max_depth:
                    asyncio.create_task(
                        self._crawl_url(link_url, depth + 1, url)
                    )

    async def crawl(self, urls: List[str]):
        """Main crawl method."""
        # Setup proxy if provided
        connector_kwargs = {'ssl': self._get_ssl_context()}
        
        connector = aiohttp.TCPConnector(**connector_kwargs)
        timeout = ClientTimeout(
            total=self.timeout if self.timeout > 0 else None
        )

        async with ClientSession(
            connector=connector, timeout=timeout
        ) as session:
            self.session = session

            tasks = []
            for url in urls:
                task = asyncio.create_task(self._crawl_url(url, 0))
                tasks.append(task)

            await asyncio.gather(*tasks, return_exceptions=True)

    def format_output(self) -> str:
        """Format results for output."""
        if self.json_output:
            results_data = []
            for result in self.results:
                results_data.append(result.to_dict())
            return json.dumps(results_data, indent=2)
        else:
            output_lines = []
            for result in self.results:
                line = result.url
                if self.show_source:
                    line = f"[{result.source}] {line}"
                if self.show_where and result.where:
                    line = f"[{result.where}] {line}"
                output_lines.append(line)
            return '\n'.join(output_lines)


def parse_headers(headers_str: str) -> Dict[str, str]:
    """Parse custom headers from string."""
    headers = {}
    if not headers_str:
        return headers

    for header in headers_str.split(';;'):
        if ':' in header:
            key, value = header.split(':', 1)
            headers[key.strip()] = value.strip()

    return headers


async def main():
    parser = argparse.ArgumentParser(
        description='Python Web Crawler - hakrawler-inspired crawler'
    )

    parser.add_argument(
        '-d', type=int, default=2,
        help='Depth to crawl (default: 2)'
    )
    parser.add_argument(
        '-dr', action='store_true',
        help='Disable following HTTP redirects'
    )
    parser.add_argument(
        '--headers', type=str, default='',
        help='Custom headers separated by two semi-colons'
    )
    parser.add_argument(
        '-i', action='store_true',
        help='Only crawl inside path'
    )
    parser.add_argument(
        '-insecure', action='store_true',
        help='Disable TLS verification'
    )
    parser.add_argument(
        '-json', action='store_true',
        help='Output as JSON'
    )
    parser.add_argument(
        '-proxy', type=str, default='',
        help='Proxy URL (e.g., http://127.0.0.1:8080)'
    )
    parser.add_argument(
        '-s', action='store_true',
        help='Show the source of URL'
    )
    parser.add_argument(
        '-size', type=int, default=-1,
        help='Page size limit, in KB'
    )
    parser.add_argument(
        '-subs', action='store_true',
        help='Include subdomains for crawling'
    )
    parser.add_argument(
        '-t', type=int, default=8,
        help='Number of threads to utilize (default: 8)'
    )
    parser.add_argument(
        '-timeout', type=int, default=-1,
        help='Maximum time to crawl each URL, in seconds'
    )
    parser.add_argument(
        '-u', action='store_true',
        help='Show only unique URLs'
    )
    parser.add_argument(
        '-w', action='store_true',
        help='Show at which link the URL is found'
    )

    args = parser.parse_args()

    # Check for stdin input
    if sys.stdin.isatty():
        print(
            "No URLs detected. Hint: echo 'https://example.com' | "
            "python python_webcrawler.py",
            file=sys.stderr
        )
        sys.exit(1)

    # Read URLs from stdin
    urls = []
    for line in sys.stdin:
        url = line.strip()
        if url:
            urls.append(url)

    if not urls:
        print("No valid URLs provided", file=sys.stderr)
        sys.exit(1)

    # Parse custom headers
    custom_headers = parse_headers(args.headers)

    # Create crawler
    crawler = PythonWebCrawler(
        max_depth=args.d,
        max_threads=args.t,
        max_size=args.size,
        insecure=args.insecure,
        subs=args.subs,
        inside=args.i,
        show_source=args.s,
        show_where=args.w,
        json_output=args.json,
        unique=args.u,
        proxy=args.proxy,
        timeout=args.timeout,
        disable_redirects=args.dr,
        custom_headers=custom_headers
    )

    # Start crawling
    await crawler.crawl(urls)

    # Output results
    output = crawler.format_output()
    if output:
        print(output)
    else:
        print(
            "No URLs were found. This usually happens when a domain is specified "
            "(https://example.com), but it redirects to a subdomain "
            "(https://www.example.com). The subdomain is not included in the "
            "scope, so no URLs are printed. In order to overcome this, either "
            "specify the final URL in the redirect chain or use the -subs option "
            "to include subdomains.",
            file=sys.stderr
        )


if __name__ == '__main__':
    asyncio.run(main())
