#!/usr/bin/env python3
"""
convert_html_to_markdown.py - Convert HTML content from a URL to Markdown format

Usage:
    python scripts/convert_html_to_markdown.py <url> [--output <output_file>]

Arguments:
    url                 The URL of the webpage to convert
    --output            Optional output file path (defaults to stdout)

Example:
    python scripts/convert_html_to_markdown.py https://example.com --output ./reports/my_task/knowledge/example_com.md
"""

import argparse
import os
import sys
import requests
from bs4 import BeautifulSoup
import html2text
import re
from urllib.parse import urlparse

def clean_filename(url):
    """Generate a clean filename from a URL"""
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/").replace("/", "_")
    if not path:
        return f"{domain}.md"
    return f"{domain}_{path}.md"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert HTML content from a URL to Markdown format')
    parser.add_argument('url', help='The URL of the webpage to convert')
    parser.add_argument('--output', help='Output file path (defaults to stdout)')
    
    args = parser.parse_args()
    
    try:
        # Fetch the webpage
        print(f"Fetching content from {args.url}...", file=sys.stderr)
        response = requests.get(args.url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "No Title"
        
        # Convert to Markdown
        h2t = html2text.HTML2Text()
        h2t.ignore_links = False
        h2t.ignore_images = False
        h2t.ignore_tables = False
        h2t.body_width = 0  # No wrapping
        
        markdown = h2t.handle(response.text)
        
        # Add metadata
        metadata = f"""---
title: {title}
source_url: {args.url}
date_accessed: {response.headers.get('Date', 'Unknown')}
---

# {title}

*Source: [{args.url}]({args.url})*

"""
        
        full_content = metadata + markdown
        
        # Output
        if args.output:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(args.output), exist_ok=True)
            
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(full_content)
            print(f"Markdown content saved to {args.output}", file=sys.stderr)
        else:
            print(full_content)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
