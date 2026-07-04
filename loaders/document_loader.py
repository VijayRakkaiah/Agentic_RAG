from pathlib import Path
from parsers.parser_factory import get_parser


def load_documents(upload_dir: str = "./data"):

    upload_path = Path(upload_dir)

    documents = []

    for file_path in upload_path.rglob("*"):

        if not file_path.is_file():
            continue

        parser = get_parser(file_path)

        doc = parser(file_path)

        documents.append(doc)

    return documents