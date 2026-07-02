import json
import os
import re

templates = [
    r"c:\Users\abala\OneDrive\Desktop\blue-minded-people-02-07-2026\Blue-minded-people\templates\index.json",
    r"c:\Users\abala\OneDrive\Desktop\blue-minded-people-02-07-2026\Blue-minded-people\templates\product.json"
]

def strip_comments(text):
    return re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

for filepath in templates:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        clean_content = strip_comments(content).strip()
        try:
            json.loads(clean_content)
            print(f"SUCCESS: {os.path.basename(filepath)} is valid JSON.")
        except json.JSONDecodeError as e:
            print(f"FAILED: {os.path.basename(filepath)} is invalid JSON:")
            print(e)
            lines = clean_content.splitlines()
            err_line = e.lineno
            start_line = max(0, err_line - 5)
            end_line = min(len(lines), err_line + 5)
            print("--- CONTEXT ---")
            for i in range(start_line, end_line):
                marker = ">>>" if i + 1 == err_line else "   "
                print(f"{marker} {i+1}: {lines[i]}")
            print("----------------")
