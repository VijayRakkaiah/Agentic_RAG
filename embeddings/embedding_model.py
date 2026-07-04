from langchain_openai import OpenAIEmbeddings
from config.settings import OPENAI_API_KEY


def get_embedding_model(model: str = "text-embedding-3-small") -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
        model=model,
    )