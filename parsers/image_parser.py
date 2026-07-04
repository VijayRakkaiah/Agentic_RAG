from PIL import Image
import pytesseract

# ---------- Image Parser ----------
def image_parser(filepath):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img = Image.open(filepath)
    text = pytesseract.image_to_string(image=img)

    return {
        "text": text,
        "metadata": {
            "file_name": filepath.name
        }
    }