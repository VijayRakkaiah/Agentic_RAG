from loaders.document_loader import load_documents
from ingestion.chunk_documents import chunk_documents
from ingestion.prepare_records import prepare_records
from vectordb.milvus_client import MilvusDB


def run_ingestion(
    data_path: str = "./data",
    collection_name: str = "enterprise_rag",
):
    """
    Execute the complete RAG ingestion pipeline.
    """

    # Step 1
    print("Loading documents...")
    documents = load_documents(data_path)

    # Step 2
    print("Chunking documents...")
    chunked_documents = chunk_documents(documents)

    # Step 3
    print("Generating embeddings...")
    records = prepare_records(chunked_documents)

    # Step 4
    print("Connecting to Milvus...")
    db = MilvusDB(collection_name)

    # Step 5
    db.create_collection()

    # Step 6
    print("Uploading vectors...")
    db.insert_records(records)

    print("Ingestion completed successfully.")