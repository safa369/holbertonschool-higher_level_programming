#!/usr/bin/python3
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filname = "add_item.json"
with open(filname, 'a+', encoding="utf8") as f:
    arguments = sys.argv[1:]
    file = load_from_json_file(filname)
    file.append(arguments)
    save_to_json_file(file, filname)
