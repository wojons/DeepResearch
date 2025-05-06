#!/usr/bin/env python3
"""
update_research_index.py - Update the central research_index.json file with a new report entry

Usage:
    python scripts/update_research_index.py <task_name> [--title "Custom Title"] [--date "YYYY-MM-DD"] [--summary "Brief summary"]

Arguments:
    task_name           The name of the research task (folder name in reports/)
    --title             Optional custom title (defaults to task_name with spaces instead of underscores)
    --date              Optional date (defaults to current date in YYYY-MM-DD format)
    --summary           Optional brief summary (defaults to extracting from report.md)

Example:
    python scripts/update_research_index.py AI_YouTube_Script_Techniques_v3 --title "AI YouTube Script Techniques" --summary "Research on AI-driven techniques for YouTube scripts"
"""

import argparse
import json
import os
import sys
from datetime import datetime

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Update research_index.json with a new report entry')
    parser.add_argument('task_name', help='The name of the research task (folder name in reports/)')
    parser.add_argument('--title', help='Custom title (defaults to task_name with spaces)')
    parser.add_argument('--date', help='Date in YYYY-MM-DD format (defaults to today)')
    parser.add_argument('--summary', help='Brief summary (defaults to extracting from report.md)')
    
    args = parser.parse_args()
    
    # Validate task_name and check if report exists
    report_path = f"reports/{args.task_name}/report.md"
    if not os.path.exists(report_path):
        print(f"Error: Report file not found at {report_path}")
        sys.exit(1)
    
    # Set defaults if not provided
    title = args.title if args.title else args.task_name.replace('_', ' ')
    date = args.date if args.date else datetime.now().strftime('%Y-%m-%d')
    
    # If summary not provided, try to extract from report.md (first paragraph)
    summary = args.summary
    if not summary:
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple extraction of first paragraph (could be improved)
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                # Skip headings and find first real paragraph
                for p in paragraphs:
                    if not p.startswith('#') and len(p) > 30:  # Arbitrary min length
                        summary = p[:200] + '...' if len(p) > 200 else p
                        break
                if not summary:
                    summary = "No summary available"
        except Exception as e:
            print(f"Warning: Could not extract summary from report: {e}")
            summary = "No summary available"
    
    # Prepare the new entry
    new_entry = {
        "task_name": args.task_name,
        "title": title,
        "date": date,
        "summary": summary,
        "report_path": report_path
    }
    
    # Read existing index file or create new one
    index_path = "index/research_index.json"
    index_data = []
    
    try:
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                index_data = json.load(f)
                if not isinstance(index_data, list):
                    print("Warning: Index file is not an array, initializing as empty list")
                    index_data = []
    except Exception as e:
        print(f"Warning: Could not read or parse {index_path}, initializing: {e}")
        index_data = []
    
    # Update existing entry or add new one
    updated = False
    for i, entry in enumerate(index_data):
        if entry.get('task_name') == args.task_name:
            index_data[i] = new_entry
            updated = True
            break
    
    if not updated:
        index_data.append(new_entry)
    
    # Write updated index back to file
    try:
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2)
        print(f"Successfully updated {index_path} for task {args.task_name}")
    except Exception as e:
        print(f"Error updating {index_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
