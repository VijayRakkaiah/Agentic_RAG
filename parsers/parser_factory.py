from pathlib import Path

from parsers.pdf_parser import pdf_parser
from parsers.csv_parser import csv_parser
from parsers.json_parser import json_parser
from parsers.pptx_parser import pptx_parser
from parsers.image_parser import image_parser

PARSER_MAP = {
    ".pdf": pdf_parser,
    ".csv": csv_parser,
    ".json": json_parser,
    ".ppt": pptx_parser,
    ".pptx": pptx_parser,
    ".png": image_parser,
    ".jpg": image_parser,
    ".jpeg": image_parser,
}


def get_parser(file_path):

    extension = Path(file_path).suffix.lower()

    parser = PARSER_MAP.get(extension)

    if parser is None:
        raise ValueError(f"Unsupported file type: {extension}")

    return parser