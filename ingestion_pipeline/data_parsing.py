from pathlib import Path
from parsers import pdf_parser, json_parser, csv_parser, ppt_parser, image_parser

UPLOAD_DIR = Path('./data')

all_files = []

for i in UPLOAD_DIR.rglob("*"):
    if i.is_file():
        all_files.append(i)

print("Length of all files is:", len(all_files))

print(all_files)

PARSERS = {
    ".pdf": pdf_parser,
    ".json": json_parser,
    ".csv": csv_parser,
    ".ppt": ppt_parser,
    ".pptx": ppt_parser,
    ".png": image_parser,
    ".jpg": image_parser,
    ".jpeg": image_parser,
}

documents = []

for file in all_files:

    print(file)
    extension = file.suffix.lower()
    parser = PARSERS.get(extension)

    if parser is None:
        print(f"Skipping {file.name}")
        continue

    doc = parser(file)
    documents.append(doc)