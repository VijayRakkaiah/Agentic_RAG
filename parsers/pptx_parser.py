from unstructured.partition.auto import partition

# ---------- PPTX Parser ----------
def pptx_parser(filepath):
    elements = partition(filename=str(filepath))

    text = "\n".join(
        element.text.strip()
        for element in elements
        if hasattr(element, "text") and element.text
    )

    return {
        "text": text,
        "metadata": {
            "file_name": filepath.name
        }
    }