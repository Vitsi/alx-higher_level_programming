#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    # Load existing data if the file exists
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, filename)
