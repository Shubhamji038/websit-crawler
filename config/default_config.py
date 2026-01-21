"""
Default configuration for Python Web Crawler
"""

# Default crawler settings
DEFAULT_CRAWLER_CONFIG = {
    "max_depth": 2,
    "max_threads": 8,
    "max_size": -1,  # KB, -1 for unlimited
    "timeout": -1,   # seconds, -1 for no timeout
    "insecure": False,
    "subs": False,
    "inside": False,
    "show_source": False,
    "show_where": False,
    "json_output": False,
    "unique": True,
    "disable_redirects": False,
    "custom_headers": {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
    }
}

# Export format configurations
EXPORT_FORMATS = {
    "txt": {
        "extension": ".txt",
        "content_type": "text/plain",
        "description": "Plain text URL list"
    },
    "json": {
        "extension": ".json", 
        "content_type": "application/json",
        "description": "JSON with metadata"
    },
    "csv": {
        "extension": ".csv",
        "content_type": "text/csv", 
        "description": "CSV spreadsheet format"
    }
}

# GUI presets
GUI_PRESETS = {
    "quick": {
        "name": "Quick Scan",
        "depth": 2,
        "threads": 4,
        "timeout": 30,
        "description": "Fast scanning with basic options"
    },
    "deep": {
        "name": "Deep Scan", 
        "depth": 5,
        "threads": 8,
        "timeout": 60,
        "description": "Comprehensive scanning with more depth"
    },
    "stealth": {
        "name": "Stealth Scan",
        "depth": 3,
        "threads": 2,
        "timeout": 120,
        "headers": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        },
        "description": "Low-profile scanning"
    }
}

# URL patterns to exclude
EXCLUDE_PATTERNS = [
    r'javascript:',
    r'mailto:',
    r'tel:',
    r'#.*',
    r'\.pdf$',
    r'\.jpg$',
    r'\.png$',
    r'\.gif$',
    r'\.css$',
    r'\.ico$'
]

# File size limits (in KB)
SIZE_LIMITS = {
    "small": 100,    # 100KB
    "medium": 500,   # 500KB  
    "large": 1000,   # 1MB
    "unlimited": -1
}

# Timeout presets (in seconds)
TIMEOUT_PRESETS = {
    "fast": 10,
    "normal": 30,
    "slow": 60,
    "none": -1
}
