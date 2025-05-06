import json
import sys
from datetime import datetime

index_file_path = "index/source_index.json"
new_entry_json = sys.argv[1]

try:
    with open(index_file_path, 'r', encoding='utf-8') as f:
        try:
            index_data = json.load(f)
            if not isinstance(index_data, list):
                print(f"Warning: {index_file_path} is not a list, initializing as empty list.")
                index_data = []
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from {index_file_path}, initializing as empty list.")
            index_data = []
except FileNotFoundError:
    print(f"Warning: {index_file_path} not found, initializing as empty list.")
    index_data = []
except Exception as e:
    print(f"Error reading {index_file_path}: {e}")
    sys.exit(1)

try:
    new_entry = json.loads(new_entry_json)
    index_data.append(new_entry)
except json.JSONDecodeError:
    print(f"Error decoding new entry JSON: {new_entry_json}")
    sys.exit(1)

try:
    with open(index_file_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2)
    print(f"Successfully updated {index_file_path}")
except Exception as e:
    print(f"Error writing to {index_file_path}: {e}")
    sys.exit(1)
