#!/usr/bin/python3
"""module to add, save, and load"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        argm = sys.argv[1:]
        filename = "add_item.json"
        file = load_from_json_file(filename)
        file.extend(argm)
        save_to_json_file(file, filename)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = argm
        save_to_json_file(file, filename)
