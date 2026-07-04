from pymilvus import MilvusClient, DataType
from config.settings import (
    ZILLIZ_URI,
    ZILLIZ_TOKEN,
)


class MilvusDB:

    def __init__(self, collection_name: str, dimension: int = 1536):

        self.collection_name = collection_name
        self.dimension = dimension

        self.client = MilvusClient(
            uri=ZILLIZ_URI,
            token=ZILLIZ_TOKEN,
        )

    def collection_exists(self) -> bool:
        collections = self.client.list_collections()
        return self.collection_name in collections

    def create_collection(self):

        if self.collection_exists():
            print(f"Collection '{self.collection_name}' already exists.")
            return

        schema = self.client.create_schema()

        schema.add_field(
            field_name="id",
            datatype=DataType.VARCHAR,
            is_primary=True,
            max_length=36,
        )

        schema.add_field(
            field_name="vector",
            datatype=DataType.FLOAT_VECTOR,
            dim=self.dimension,
        )

        schema.add_field(
            field_name="text",
            datatype=DataType.VARCHAR,
            max_length=65535,
        )

        schema.add_field(
            field_name="file_name",
            datatype=DataType.VARCHAR,
            max_length=255,
        )

        schema.add_field(
            field_name="chunk_id",
            datatype=DataType.INT64,
        )

        index_params = self.client.prepare_index_params()

        index_params.add_index(
            field_name="vector",
            index_type="AUTOINDEX",
            metric_type="COSINE",
        )

        self.client.create_collection(
            collection_name=self.collection_name,
            schema=schema,
            index_params=index_params,
        )

        print(f"Collection '{self.collection_name}' created successfully.")

    def insert_records(self, records: list):

        if not records:
            print("No records to insert.")
            return

        self.client.insert(
            collection_name=self.collection_name,
            data=records,
        )

        print(f"{len(records)} records inserted successfully.")

    def delete_collection(self):

        if self.collection_exists():

            self.client.drop_collection(self.collection_name)

            print(f"Collection '{self.collection_name}' deleted.")

    def get_client(self):

        return self.client