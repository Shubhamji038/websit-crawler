#!/usr/bin/env python3
"""
Setup script for Python Web Crawler
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'docs', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Python Web Crawler - A comprehensive web crawling solution"

# Read requirements
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'src', 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return ['aiohttp>=3.8.0', 'beautifulsoup4>=4.11.0', 'lxml>=4.9.0']

setup(
    name="python-webcrawler",
    version="1.0.0",
    author="Shubham",
    description="A comprehensive web crawling solution inspired by hakrawler",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shubhamji038/python-webcrawler",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.18",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
        "gui": [
            "tkinter",  # Usually included with Python
        ]
    },
    entry_points={
        "console_scripts": [
            "webcrawler=webcrawler:main",
            "webcrawler-cli=python_webcrawler:main",
        ],
        "gui_scripts": [
            "webcrawler-gui=webcrawler:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.bat"],
    },
    zip_safe=False,
    keywords="web crawler scraping hakrawler async",
    project_urls={
        "Bug Reports": "https://github.com/Shubhamji038/python-webcrawler/issues",
        "Source": "https://github.com/Shubhamji038/python-webcrawler",
        "Documentation": "https://github.com/Shubhamji038/python-webcrawler/wiki",
    },
)
