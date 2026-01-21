# 🕷️ Python Web Crawler Documentation

This directory contains detailed documentation for the Python Web Crawler project.

## 📚 Documentation Files

### Main Documentation
- **README.md** (root) - Main project documentation and quick start guide
- **CONTRIBUTING.md** - Contributing guidelines and development setup
- **LICENSE** - MIT License information

### API Documentation
- **Core Crawler** (`src/python_webcrawler.py`) - Async web crawling engine
- **GUI Interface** (`src/webcrawler.py`) - User-friendly interface
- **Configuration** (`config/default_config.py`) - Default settings and presets

### Examples
- **Basic Usage** (`examples/basic_usage.py`) - Core crawler examples
- **GUI Examples** (`examples/gui_usage.py`) - Interface demonstrations

## 🔧 Development Documentation

### Project Structure
```
websit-crawler/
├── src/                    # Source code
├── tests/                  # Test suite
├── examples/               # Usage examples
├── docs/                   # Documentation
├── config/                 # Configuration files
└── .github/workflows/      # CI/CD pipelines
```

### Setup and Installation
1. Clone the repository
2. Install dependencies: `pip install -e ".[dev,gui]"`
3. Run tests: `make test`
4. Start GUI: `python src/webcrawler.py`

## 🌐 Online Resources

- **GitHub Repository**: https://github.com/Shubhamji038/python-webcrawler
- **Issues & Support**: https://github.com/Shubhamji038/python-webcrawler/issues
- **Wiki**: https://github.com/Shubhamji038/python-webcrawler/wiki

## 📖 Usage Guides

### Quick Start
1. Double-click `RUN.bat` for GUI
2. Choose scan type (Instant, Quick, Advanced, Batch)
3. Enter URL and configure options
4. Export results in preferred format

### Command Line
```bash
# Basic usage
echo "https://example.com" | python src/python_webcrawler.py

# Advanced options
echo "https://example.com" | python src/python_webcrawler.py -d 3 -s -json
```

### Python API
```python
from src.python_webcrawler import PythonWebCrawler
import asyncio

async def crawl():
    crawler = PythonWebCrawler(max_depth=2)
    await crawler.crawl(["https://example.com"])
    print(crawler.results)

asyncio.run(crawl())
```

### 📋 All-in-One Interface
- **Instant Scan** - One-click scanning with automatic export
- **Quick Scan** - Basic options with format choice
- **Advanced Scan** - Full control over all parameters
- **Batch Scan** - Process multiple URLs at once
- **Export Options** - TXT, JSON, CSV formats
- **Result Management** - View and export previous results

### ⚡ Instant Scan
- Enter URL → Scan → Export automatically
- Depth 2, clean URL list
- Automatic filename based on URL

### 🚀 Quick Scan
- Choose depth (1-3)
- Select export format (TXT/JSON/CSV)
- Custom filename
- Preview results

### ⚙️ Advanced Scan
- Complete control over all options
- Depth control (1-10)
- Thread management (1-20)
- Timeout and size limits
- Subdomain inclusion
- Path restriction
- Custom headers
- Proxy support
- TLS options

### 📦 Batch Scan
- Multiple URLs at once
- Consistent settings across all
- Grouped results by source URL

## 🛠️ Requirements

```bash
pip install -r requirements.txt
```

## 📁 Files

- `RUN.bat` - Main launcher (double-click this)
- `webcrawler.py` - Unified interface with all features
- `python_webcrawler.py` - Core crawler engine
- `requirements.txt` - Dependencies

## 🎯 Use Cases

- **Website Analysis** - Discover site structure quickly
- **Security Reconnaissance** - Find hidden endpoints
- **SEO Audits** - Comprehensive site mapping
- **Competitive Analysis** - Analyze multiple sites

## 📊 What It Finds

- **[href]** - Regular links and navigation
- **[script]** - JavaScript files
- **[form]** - Form action URLs

## 🔧 Command Line Usage

You can also use the core crawler directly:

```bash
# Basic usage
echo "https://example.com" | python python_webcrawler.py

# Advanced usage
echo "https://example.com" | python python_webcrawler.py -d 3 -s -json

# With custom headers
echo "https://example.com" | python python_webcrawler.py --headers "User-Agent: Bot/1.0"

# With proxy
echo "https://example.com" | python python_webcrawler.py -proxy http://127.0.0.1:8080
```

## 🚨 Tips

- **Instant Scan** for fastest results
- **Quick Scan** for format control
- **Advanced Scan** for complete control
- **Batch Scan** for multiple sites
- Use depth 1-2 for quick scans
- Use depth 3+ for comprehensive analysis

## 📚 Examples

### Using the Unified Interface
```
Double-click RUN.bat
Choose option 1 (Instant Scan)
Enter: https://example.com
Results saved to: example.com.txt
```

### Command Line Examples
```bash
# Instant scan equivalent
echo "https://example.com" | python python_webcrawler.py -d 2

# Deep analysis
echo "https://example.com" | python python_webcrawler.py -d 3 -subs -json

# Security reconnaissance
echo "https://example.com" | python python_webcrawler.py -d 4 -s -w
```

Perfect for both beginners and power users! 🎊
