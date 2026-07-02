import json
import re
import os

files = [
    r"c:\Users\abala\OneDrive\Desktop\blue-minded-people-02-07-2026\Blue-minded-people\sections\pdp-trust-scroll-strip.liquid",
    r"c:\Users\abala\OneDrive\Desktop\blue-minded-people-02-07-2026\Blue-minded-people\sections\category-explore-banner.liquid",
    r"c:\Users\abala\OneDrive\Desktop\blue-minded-people-02-07-2026\Blue-minded-people\sections\related-products-carousel.liquid"
]

for filepath in files:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
    if not match:
        print(f"No schema block found in: {filepath}")
        continue
        
    schema_str = match.group(1).strip()
    try:
        data = json.loads(schema_str)
        print(f"SUCCESS: {os.path.basename(filepath)} has a valid JSON schema.")
    except json.JSONDecodeError as e:
        print(f"FAILED: {os.path.basename(filepath)} has invalid schema JSON:")
        print(e)
        # Show lines around the error
        lines = schema_str.splitlines()
        err_line = e.lineno
        start_line = max(0, err_line - 5)
        end_line = min(len(lines), err_line + 5)
        print("--- CONTEXT ---")
        for i in range(start_line, end_line):
            marker = ">>>" if i + 1 == err_line else "   "
            print(f"{marker} {i+1}: {lines[i]}")
        print("----------------")
