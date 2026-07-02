from langchain_text_splitters import RecursiveCharacterTextSplitter

spiltter = RecursiveCharacterTextSplitter(
    chunk_size = 600,
    chunk_overlap = 100
)


