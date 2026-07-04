import uuid
from typing import List

from langchain_core.documents import Document

from embeddings.embedding_model import get_embedding_model


def prepare_records(
    chunked_documents: List[Document],
) -> list[dict]:
    """
    Convert LangChain Documents into Milvus records.
    """

    embedding_model = get_embedding_model()

    texts = [
        chunk.page_content
        for chunk in chunked_documents
    ]

    vectors = embedding_model.embed_documents(texts)

    records = []

    for chunk, vector in zip(chunked_documents, vectors):

        records.append(
            {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "text": chunk.page_content,
                "file_name": chunk.metadata["file_name"],
                "chunk_id": chunk.metadata["chunk_id"],
            }
        )

    return records