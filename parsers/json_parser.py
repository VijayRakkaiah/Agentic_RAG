import json

# ---------- JSON Parser ----------
def json_parser(filepath):

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return {
        "text": json.dumps(data, indent=2),
        "metadata": {
            "file_name":filepath.name
        }
    }