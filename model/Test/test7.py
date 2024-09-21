import re
import json

def extract_json(content):
    json_block = re.search(r'```json(.*?)```', content, re.DOTALL)
    if json_block:
        json_str = json_block.group(1).strip()
        try:
            parsed_json = json.loads(json_str)
            return parsed_json
        except json.JSONDecodeError:
            print("Invalid JSON within the block.")
            return None

    content = content.strip()
    if content.startswith("{") and content.endswith("}"):
        try:
            parsed_json = json.loads(content)
            return parsed_json
        except json.JSONDecodeError:
            print("Content starts with `{`, but it's not valid JSON.")
            return None

    return None


# Example input with mixed content
input_content = """
Here is the JSON response for the invoice you provided:
```json
{
  "bill_amount": 63.00,
  "invoice_category": "Retail Invoice",
  "additional_information": {
    "bill_no": "2350",
    "cashier": "Diler",
    "products": [
      {
        "product_name": "Adrak Chai",
        "quantity": 70,
        "sub_total": 60.00,
        "cgst": 250,
        "sgst": 2.50
      }
    ]
  }
}
```
"""
print(extract_json(input_content))