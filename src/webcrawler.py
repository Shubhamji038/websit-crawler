#!/usr/bin/env python3
"""
Streamlined Web Crawler Interface
Simple step-by-step crawling
"""

import asyncio
import json
import csv
import os
from python_webcrawler import PythonWebCrawler, parse_headers


class StreamlinedWebCrawler:
    def __init__(self):
        self.last_results = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print("=" * 50)
        print("PYTHON WEB CRAWLER")
        print("=" * 50)

    def show_scan_types(self):
        print("\nSELECT SCAN TYPE:")
        print("1. Instant Scan")
        print("2. Quick Scan") 
        print("3. Advanced Scan")
        print("4. Batch Scan")
        print("5. Exit")

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
            except (ValueError, EOFError, KeyboardInterrupt):
                if default is not None:
                    return default
                else:
                    return None
            except Exception as e:
                print(f"[!] An error occurred: {e}")
                if default is not None:
                    return default
                else:
                    return None

    def get_urls_input(self, scan_type):
        """Get URLs based on scan type"""
        urls = []
        
        if scan_type == 4:  # Batch Scan
            print("\nEnter multiple URLs (one per line). Enter 'done' when finished:")
            while True:
                url = input(f"URL {len(urls) + 1}: ").strip()
                if url.lower() == 'done':
                    break
                if url:
                    urls.append(url)
        else:  # Single URL scans
            url = self.get_input("Enter website URL")
            if url:
                urls.append(url)
        
        return urls

    def get_scan_options(self, scan_type):
        """Get scan options based on scan type"""
        options = {}
        
        if scan_type == 1:  # Instant Scan
            options['max_depth'] = 2
            options['show_source'] = False
            options['unique'] = True
            options['live_output'] = True
            
        elif scan_type == 2:  # Quick Scan
            options['max_depth'] = self.get_input("Crawl depth (1-3)", 2, int)
            options['max_depth'] = max(1, min(3, options['max_depth']))
            options['show_source'] = True
            options['unique'] = True
            options['live_output'] = True
            
        elif scan_type == 3:  # Advanced Scan
            print("\n--- ADVANCED OPTIONS ---")
            options['max_depth'] = self.get_input("Crawl depth (1-10)", 2, int)
            options['max_depth'] = max(1, min(10, options['max_depth']))
            options['max_threads'] = self.get_input("Number of threads (1-20)", 8, int)
            options['timeout'] = self.get_input("Timeout per URL (seconds, -1 for none)", -1, int)
            options['max_size'] = self.get_input("Page size limit in KB (-1 for unlimited)", -1, int)
            
            print("\n--- FILTERING OPTIONS ---")
            options['subs'] = self.get_input("Include subdomains? (y/n)", False, bool)
            options['inside'] = self.get_input("Stay inside path only? (y/n)", False, bool)
            options['unique'] = self.get_input("Show only unique URLs? (y/n)", True, bool)
            
            print("\n--- OUTPUT OPTIONS ---")
            options['show_source'] = self.get_input("Show source types? (y/n)", False, bool)
            options['show_where'] = self.get_input("Show where URLs were found? (y/n)", False, bool)
            options['json_output'] = self.get_input("JSON output format? (y/n)", False, bool)
            
            print("\n--- SECURITY OPTIONS ---")
            options['insecure'] = self.get_input("Skip TLS verification? (y/n)", False, bool)
            options['disable_redirects'] = self.get_input("Disable redirects? (y/n)", False, bool)
            
            proxy = self.get_input("Proxy URL (optional)", "")
            options['proxy'] = proxy if proxy else None
            
            headers_input = self.get_input("Custom headers (format: 'Header: Value;;Header2: Value2')", "")
            options['custom_headers'] = parse_headers(headers_input) if headers_input else {}
            options['live_output'] = True
            
        elif scan_type == 4:  # Batch Scan
            options['max_depth'] = self.get_input("Crawl depth (1-5)", 2, int)
            options['max_depth'] = max(1, min(5, options['max_depth']))
            options['show_source'] = True
            options['unique'] = True
            options['live_output'] = True
        
        return options

    def run_crawl(self, scan_type, urls, options):
        """Execute the crawl with given options"""
        print(f"\n[*] Starting crawl...")
        print(f"[*] URLs to scan: {len(urls)}")
        print(f"[*] Depth: {options['max_depth']}")
        print("[*] Live results:")
        print("-" * 50)

        crawler = PythonWebCrawler(**options)
        asyncio.run(crawler.crawl(urls))
        
        self.last_results = crawler.results
        
        if not crawler.results:
            print("\n[!] No results found")
            return False
        
        print(f"\n[+] Crawl completed! Found {len(crawler.results)} URLs")
        return True

    def ask_to_save(self, scan_type):
        """Ask user if they want to save results"""
        if not self.last_results:
            print("[!] No results to save")
            return

        save_choice = self.get_input("Do you want to save the results? (y/n)", True, bool)
        
        if not save_choice:
            print("[*] Results not saved.")
            return

        # Get filename
        if scan_type == 1:  # Instant Scan
            default_name = "instant_scan"
        elif scan_type == 2:  # Quick Scan
            default_name = "quick_scan"
        elif scan_type == 3:  # Advanced Scan
            default_name = "advanced_scan"
        else:  # Batch Scan
            default_name = "batch_scan"

        filename = self.get_input("Enter filename (without extension)", default_name)
        
        # Get format
        print("\nSelect export format:")
        print("1. TXT (URL list)")
        print("2. JSON (with metadata)")
        print("3. CSV (spreadsheet)")
        format_choice = self.get_input("Choose format (1-3)", 1, int)
        
        format_map = {1: "txt", 2: "json", 3: "csv"}
        export_format = format_map.get(format_choice, "txt")
        
        self.export_results(filename, export_format)

    def export_results(self, filename, export_format):
        """Export results to file"""
        # Ensure output directory exists
        output_dir = os.path.join("..", "output")
        os.makedirs(output_dir, exist_ok=True)

        try:
            if export_format == "txt":
                filepath = os.path.join(output_dir, f"{filename}.txt")
                with open(filepath, 'w', encoding='utf-8') as f:
                    for result in self.last_results:
                        f.write(f"{result.url}\n")
                print(f"[*] Saved: {filename}.txt")

            elif export_format == "json":
                data = [result.to_dict() for result in self.last_results]
                filepath = os.path.join(output_dir, f"{filename}.json")
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"[*] Saved: {filename}.json")

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
                print(f"[*] Saved: {filename}.csv")

        except Exception as e:
            print(f"\n[!] Export failed: {e}")

    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.print_header()
            self.show_scan_types()

            choice = self.get_input("\nEnter your choice (1-5)", 1, int)
            
            if choice == 5:
                print("\n[*] Goodbye!")
                break
            
            if choice not in [1, 2, 3, 4]:
                print("[!] Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
                continue

            # Get URLs
            urls = self.get_urls_input(choice)
            if urls is None or not urls:
                print("[!] No URLs provided or input cancelled.")
                input("\nPress Enter to continue...")
                continue

            # Get options
            options = self.get_scan_options(choice)

            # Run crawl
            success = self.run_crawl(choice, urls, options)
            
            if success:
                # Ask to save
                self.ask_to_save(choice)

            input("\nPress Enter to continue...")


def main():
    try:
        crawler = StreamlinedWebCrawler()
        crawler.run()
    except KeyboardInterrupt:
        print("\n[*] Goodbye!")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")


if __name__ == "__main__":
    main()
