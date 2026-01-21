# 🕷️ Python Web Crawler

A comprehensive web crawling solution with proper project structure, inspired by hakrawler for gathering URLs and JavaScript file locations from websites.

## 📁 Project Structure

```
websit-crawler/
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── python_webcrawler.py     # Core crawler engine
│   ├── webcrawler.py            # Unified GUI interface
│   └── requirements.txt         # Dependencies
├── tests/                        # Test suite
│   ├── __init__.py
│   └── test_crawler.py          # Unit tests
├── examples/                     # Usage examples
│   ├── basic_usage.py           # Core crawler examples
│   └── gui_usage.py             # GUI examples
├── docs/                         # Documentation
│   └── README.md                # Original documentation
├── config/                       # Configuration files
│   └── default_config.py        # Default settings
├── RUN.bat                      # Windows launcher
├── setup.py                     # Package setup
├── pyproject.toml              # Modern Python packaging
├── Makefile                     # Development commands
└── .gitignore                   # Git ignore rules
```

## 🚀 Quick Start

### Option 1: Double-click Launcher
```bash
Double-click RUN.bat
```

### Option 2: Install and Run
```bash
# Install the package
pip install -e .

# Run GUI
python src/webcrawler.py

# Or use command line
echo "https://example.com" | python src/python_webcrawler.py
```

### Option 3: Development Setup
```bash
# Install with dev dependencies
make install-dev

# Run tests
make test

# Run examples
make run-examples
```

## 🎯 Features

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
pip install -r src/requirements.txt
```

## 📁 Files

- `RUN.bat` - Main launcher (double-click this)
- `src/webcrawler.py` - Unified interface with all features
- `src/python_webcrawler.py` - Core crawler engine
- `src/requirements.txt` - Dependencies

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
echo "https://example.com" | python src/python_webcrawler.py

# Advanced usage
echo "https://example.com" | python src/python_webcrawler.py -d 3 -s -json

# With custom headers
echo "https://example.com" | python src/python_webcrawler.py --headers "User-Agent: Bot/1.0"

# With proxy
echo "https://example.com" | python src/python_webcrawler.py -proxy http://127.0.0.1:8080
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
echo "https://example.com" | python src/python_webcrawler.py -d 2

# Deep analysis
echo "https://example.com" | python src/python_webcrawler.py -d 3 -subs -json

# Security reconnaissance
echo "https://example.com" | python src/python_webcrawler.py -d 4 -s -w
```

## 🛠️ Development

### Running Tests
```bash
make test
make test-coverage
```

### Code Quality
```bash
make lint        # Check code style
make format      # Format code
```

### Building Package
```bash
make build
make upload      # Upload to PyPI
```

### Examples
```bash
# Basic usage
python examples/basic_usage.py

# GUI demo
python examples/gui_usage.py
```

## 🔗 Repository Links

- **GitHub Repository**: https://github.com/Shubhamji038/websit-crawler
- **Issues & Bug Reports**: https://github.com/Shubhamji038/websit-crawler/issues
- **Documentation**: https://github.com/Shubhamji038/websit-crawler/wiki
- **Contributing**: https://github.com/Shubhamji038/websit-crawler/blob/main/CONTRIBUTING.md

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Reporting bugs
- Suggesting features  
- Submitting pull requests
- Code style and testing

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [hakrawler](https://github.com/hakluke/hakrawler)
- Built with [aiohttp](https://aiohttp.readthedocs.io/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---

**Created by [Shubham](https://github.com/Shubhamji038)** 🚀

Perfect for both beginners and power users! 🎊
