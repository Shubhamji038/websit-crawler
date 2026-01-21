#!/usr/bin/env python3
"""
Unified Web Crawler Interface
All features in one clean interface
"""

import asyncio
import json
import csv
import os
from python_webcrawler import PythonWebCrawler, parse_headers


def get_output_path(filename):
    """Get output path outside src directory"""
    return os.path.join("..", "output", filename)


class UnifiedWebCrawler:
    def __init__(self):
        self.last_results = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print("=" * 60)
        print("🕷️  PYTHON WEB CRAWLER - UNIFIED INTERFACE")
        print("=" * 60)
        print("Complete web crawling solution with all features")
        print("=" * 60)

    def show_menu(self):
        print("\n MAIN MENU:")
        print("1. Instant Scan")
        print("2. Quick Scan")
        print("3. Advanced Scan")
        print("4. Batch Scan")
        print("5. Export Last Results")
        print("6. View Last Results")
        print("7. Exit")
        print("\n EXPORT OPTIONS (add letter to scan option):")
        print("a = TXT format")
        print("b = JSON format")
        print("c = CSV format")
        print("\n DEPTH OPTIONS (add number to scan option):")
        print("1 = Depth 1")
        print("2 = Depth 2")
        print("3 = Depth 3")
        print("\n EXAMPLES:")
        print("2a = Quick Scan + TXT export")
        print("2b3 = Quick Scan + JSON export + Depth 3")
        print("3c2 = Advanced Scan + CSV export + Depth 2")
        print("-" * 60)

    def get_input(self, prompt, default=None, input_type=str):
        while True:
            try:
                if default is not None:
                    user_input = input(f"{prompt} (default: {default}): ").strip()
                    if not user_input:
                        return default
                else:
                    user_input = input(f"{prompt}: ").strip()

                if input_type == int:
                    return int(user_input)
                elif input_type == bool:
                    return user_input.lower() in ['y', 'yes', 'true', '1']
                else:
                    return user_input
            except ValueError:
                print(f"❌ Invalid input. Please enter a valid {input_type.__name__}")
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                if default is not None:
                    return default
                else:
                    raise

    def instant_scan(self):
        """Instant one-click scan"""
        print("\n⚡ INSTANT SCAN")
        print("-" * 30)

        url = self.get_input("Enter website URL")
        if not url:
            print("❌ URL is required")
            return

        filename = url.replace('https://', '').replace('http://', '').replace('/', '_')

        print(f"\n🔍 Scanning {url}...")
        print(f"📁 Will save as: {filename}.txt")
        print("-" * 40)

        crawler = PythonWebCrawler(
            max_depth=2,
            show_source=False,
            json_output=False,
            unique=True
        )

        asyncio.run(crawler.crawl([url]))

        if not crawler.results:
            print("❌ No results found")
            return

        # Export to TXT
        output_dir = os.path.join("..", "output")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, f"{filename}.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            for result in crawler.results:
                f.write(f"{result.url}\n")

        self.last_results = crawler.results

        print(f"✅ Found {len(crawler.results)} URLs")
        print(f"📁 Saved: {filename}.txt")

        # Quick preview
        print("\n📋 First few URLs:")
        for i, result in enumerate(crawler.results[:3], 1):
            print(f"{i}. {result.url}")
        if len(crawler.results) > 3:
            print(f"... and {len(crawler.results) - 3} more")

    def parse_option(self, choice):
        """Parse combined options like '2a', '2b3', '3c2'"""
        if not choice:
            return None, None, None

        # Extract main option (first digit)
        main_option = None
        export_format = None
        depth = None

        # Find the first digit for main option
        for char in choice:
            if char.isdigit():
                main_option = int(char)
                remaining = choice[choice.index(char) + 1:]
                break
        else:
            return None, None, None

        # Parse remaining characters
        for char in remaining:
            if char.lower() in ['a', 'b', 'c']:
                export_format = {'a': 'txt', 'b': 'json', 'c': 'csv'}[char.lower()]
            elif char.isdigit():
                depth = int(char)

        return main_option, export_format, depth

    def quick_scan_combined(self, export_format=None, depth=None):
        """Quick scan with pre-specified options"""
        print("\n🚀 QUICK SCAN")
        print("-" * 30)

        url = self.get_input("Enter website URL")
        if not url:
            print("❌ URL is required")
            return

        # Use provided options or ask
        if depth is None:
            depth = self.get_input("Crawl depth (1-3)", 2, int)
            depth = max(1, min(3, depth))
        else:
            depth = max(1, min(3, depth))
            print(f"Using depth: {depth}")

        if export_format is None:
            print("\nExport format:")
            print("1. TXT (URL list)")
            print("2. JSON (with metadata)")
            print("3. CSV (spreadsheet)")
            format_choice = self.get_input("Choose format (1-3)", 1, int)
            format_map = {1: "txt", 2: "json", 3: "csv"}
            export_format = format_map.get(format_choice, "txt")
        else:
            print(f"Using export format: {export_format.upper()}")

        filename = self.get_input(
            "Filename (without extension)",
            f"scan_{url.replace('https://', '').replace('/', '_')}"
        )

        print(f"\n🔍 Scanning {url}...")
        print(f"📊 Depth: {depth} | Format: {export_format.upper()}")
        print("-" * 40)

        crawler = PythonWebCrawler(
            max_depth=depth,
            show_source=True,
            json_output=(export_format == "json"),
            unique=True
        )

        asyncio.run(crawler.crawl([url]))

        if not crawler.results:
            print("❌ No results found")
            return

        self.last_results = crawler.results
        self.export_results(filename, export_format)

        print(f"\n📋 PREVIEW (first 5 items):")
        print("-" * 30)
        for i, result in enumerate(crawler.results[:5], 1):
            source_tag = f"[{getattr(result, 'source', '')}] " if hasattr(
                result, 'source'
            ) and result.source else ""
            print(f"{i}. {source_tag}{result.url}")

        if len(crawler.results) > 5:
            print(f"... and {len(crawler.results) - 5} more items")

    def advanced_scan_combined(self, export_format=None, depth=None):
        """Advanced scan with pre-specified options"""
        print("\n⚙️  ADVANCED SCAN")
        print("-" * 30)

        url = self.get_input("Enter website URL")
        if not url:
            print("❌ URL is required")
            return

        print("\n📊 CRAWL OPTIONS:")
        if depth is None:
            depth = self.get_input("Crawl depth (1-10)", 2, int)
        else:
            depth = max(1, min(10, depth))
            print(f"Using depth: {depth}")

        threads = self.get_input("Number of threads (1-20)", 8, int)
        timeout = self.get_input("Timeout per URL (seconds, -1 for none)", -1, int)
        max_size = self.get_input("Page size limit in KB (-1 for unlimited)", -1, int)

        print("\n🎯 FILTERING OPTIONS:")
        subs = self.get_input("Include subdomains? (y/n)", bool, False)
        inside = self.get_input("Stay inside path only? (y/n)", bool, False)
        unique = self.get_input("Show only unique URLs? (y/n)", bool, True)

        print("\n📤 OUTPUT OPTIONS:")
        show_source = self.get_input("Show source types? (y/n)", bool, False)
        show_where = self.get_input("Show where URLs were found? (y/n)", bool, False)
        json_output = self.get_input(
            "JSON output format? (y/n)", bool, (export_format == "json")
        )

        print("\n🔐 SECURITY OPTIONS:")
        insecure = self.get_input("Skip TLS verification? (y/n)", bool, False)
        disable_redirects = self.get_input("Disable redirects? (y/n)", bool, False)

        proxy = self.get_input("Proxy URL (optional)", str, "")
        if not proxy:
            proxy = None

        headers_input = self.get_input(
            "Custom headers (format: 'Header: Value;;Header2: Value2')", str, ""
        )
        custom_headers = parse_headers(headers_input) if headers_input else {}

        # Create crawler
        crawler = PythonWebCrawler(
            max_depth=depth,
            max_threads=threads,
            timeout=timeout,
            max_size=max_size,
            subs=subs,
            inside=inside,
            show_source=show_source,
            show_where=show_where,
            json_output=json_output,
            unique=unique,
            insecure=insecure,
            disable_redirects=disable_redirects,
            proxy=proxy,
            custom_headers=custom_headers
        )

        print(f"\n🔍 Scanning {url} with advanced settings...")
        print("-" * 40)

        asyncio.run(crawler.crawl([url]))

        if not crawler.results:
            print("❌ No results found")
            return

        self.last_results = crawler.results

        # Export options
        if export_format:
            filename = self.get_input(
                "Filename (without extension)",
                f"advanced_{url.replace('https://', '').replace('/', '_')}"
            )
            self.export_results(filename, export_format)
        else:
            export_choice = self.get_input("Export results? (y/n)", bool, True)
            if export_choice:
                filename = self.get_input(
                    "Filename (without extension)",
                    f"advanced_{url.replace('https://', '').replace('/', '_')}"
                )

                if json_output:
                    self.export_results(filename, "json")
                else:
                    format_choice = self.get_input("Format (1=TXT, 2=CSV)", 1, int)
                    export_format = "txt" if format_choice == 1 else "csv"
                    self.export_results(filename, export_format)

        print(f"\n📊 RESULTS ({len(crawler.results)} items found):")
        print("-" * 40)
        for i, result in enumerate(crawler.results[:10], 1):
            source_tag = f"[{getattr(result, 'source', '')}] " if hasattr(
                result, 'source'
            ) and result.source else ""
            where_tag = f"[{getattr(result, 'where', '')}] " if hasattr(
                result, 'where'
            ) and result.where else ""
            print(f"{i:3d}. {source_tag}{where_tag}{result.url}")

        if len(crawler.results) > 10:
            print(f"... and {len(crawler.results) - 10} more items")

    def batch_scan(self):
        """Batch scan multiple URLs"""
        print("\n📦 BATCH SCAN")
        print("-" * 30)
        print("Enter multiple URLs (one per line). Enter 'done' when finished:")

        urls = []
        while True:
            url = input(f"URL {len(urls) + 1}: ").strip()
            if url.lower() == 'done':
                break
            if url:
                urls.append(url)

        if not urls:
            print("❌ No URLs provided")
            return

        depth = self.get_input("Crawl depth (1-5)", 2, int)
        depth = max(1, min(5, depth))

        export_format = self.get_input("Export format (1=TXT, 2=JSON, 3=CSV)", 1, int)
        format_map = {1: "txt", 2: "json", 3: "csv"}
        export_format = format_map.get(export_format, "txt")

        filename = self.get_input("Filename (without extension)", "batch_scan")

        print(f"\n🔍 Scanning {len(urls)} URLs with depth {depth}...")
        print("-" * 40)

        crawler = PythonWebCrawler(
            max_depth=depth,
            show_source=True,
            json_output=(export_format == "json"),
            unique=True
        )

        asyncio.run(crawler.crawl(urls))

        if not crawler.results:
            print("❌ No results found")
            return

        self.last_results = crawler.results
        self.export_results(filename, export_format)

        print(f"\n📊 RESULTS ({len(crawler.results)} items found from {len(urls)} URLs):")
        print("-" * 40)

        # Group by URL
        url_groups = {}
        for result in crawler.results:
            base_url = next((url for url in urls if url in result.url), "Unknown")
            if base_url not in url_groups:
                url_groups[base_url] = []
            url_groups[base_url].append(result)

        for url, results in url_groups.items():
            print(f"\n🔗 {url} ({len(results)} items):")
            for i, result in enumerate(results[:3], 1):
                source_tag = f"[{getattr(result, 'source', '')}] " if hasattr(
                    result, 'source'
                ) and result.source else ""
                print(f"   {i}. {source_tag}{result.url}")
            if len(results) > 3:
                print(f"   ... and {len(results) - 3} more")

    def export_results(self, filename, export_format):
        """Export results to file"""
        if not self.last_results:
            print("❌ No results to export")
            return

        # Ensure output directory exists
        output_dir = os.path.join("..", "output")
        os.makedirs(output_dir, exist_ok=True)

        try:
            if export_format == "txt":
                filepath = os.path.join(output_dir, f"{filename}.txt")
                with open(filepath, 'w', encoding='utf-8') as f:
                    for result in self.last_results:
                        f.write(f"{result.url}\n")
                print(f"📁 Saved: {filename}.txt")

            elif export_format == "json":
                data = [result.to_dict() for result in self.last_results]
                filepath = os.path.join(output_dir, f"{filename}.json")
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"📁 Saved: {filename}.json")

            elif export_format == "csv":
                filepath = os.path.join(output_dir, f"{filename}.csv")
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['URL', 'Source', 'Where'])
                    for result in self.last_results:
                        url = result.url
                        source = getattr(result, 'source', '')
                        where = getattr(result, 'where', '')
                        writer.writerow([url, source, where])
                print(f"📁 Saved: {filename}.csv")

        except Exception as e:
            print(f"❌ Export failed: {e}")

    def view_results(self):
        """View last results"""
        if not self.last_results:
            print("\n❌ No previous results to display")
            return

        print(f"\n📊 LAST RESULTS ({len(self.last_results)} items):")
        print("-" * 40)

        for i, result in enumerate(self.last_results, 1):
            source_tag = f"[{getattr(result, 'source', '')}] " if hasattr(
                result, 'source'
            ) and result.source else ""
            where_tag = f"[{getattr(result, 'where', '')}] " if hasattr(
                result, 'where'
            ) and result.where else ""
            print(f"{i:3d}. {source_tag}{where_tag}{result.url}")

    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.print_header()
            self.show_menu()

            choice = self.get_input("Enter option (e.g., 2a, 2b3, 3c2)").strip()

            # Parse combined options
            main_option, export_format, depth = self.parse_option(choice)

            if main_option == 1:
                self.instant_scan()
            elif main_option == 2:
                self.quick_scan_combined(export_format, depth)
            elif main_option == 3:
                self.advanced_scan_combined(export_format, depth)
            elif main_option == 4:
                self.batch_scan()
            elif main_option == 5:
                filename = self.get_input("Filename (without extension)", "export")
                export_format = self.get_input("Format (1=TXT, 2=JSON, 3=CSV)", 1, int)
                format_map = {1: "txt", 2: "json", 3: "csv"}
                self.export_results(filename, format_map.get(export_format, "txt"))
            elif main_option == 6:
                self.view_results()
            elif main_option == 7:
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
                print("Examples: 2a, 2b3, 3c2")

            input("\nPress Enter to continue...")


def main():
    try:
        crawler = UnifiedWebCrawler()
        crawler.run()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
