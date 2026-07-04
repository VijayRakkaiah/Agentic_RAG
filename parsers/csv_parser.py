import pandas as pd

# ---------- CSV Parser ----------
def csv_parser(filepath):

    df = pd.read_csv(filepath)

    return {
        "text": df.to_string(index=False),
        "metadata": {
            "file_name": filepath.name
        }
    }