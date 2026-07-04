import fitz

def pdf_parser(file):
    doc = fitz.open(file)

    text = ""

    for page in doc:
        text = text + page.get_text()

    return {
        "text": text,
        "metadata": {
            "file_name": file.name
        }
    }