from typing import List
from langchain_core.documents import Document
from chunking.text_splitter import get_text_splitter


def chunk_documents(
    documents: List[dict],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> List[Document]:
    
    splitter = get_text_splitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunked_documents = []

    for doc in documents:

        text = doc.get("text", "").strip()
        metadata = doc.get("metadata", {}).copy()

        chunks = splitter.create_documents(
            texts=[text],
            metadatas=[metadata]
        )

        for index, chunk in enumerate(chunks):

            chunk.metadata["chunk_id"] = index
            chunk.metadata["total_chunks"] = len(chunks)

            chunked_documents.append(chunk)

    return chunked_documents