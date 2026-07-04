from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_text_splitter(
    chunk_size: int = 600,
    chunk_overlap: int = 100,
    separators: list[str] | None = None,
) -> RecursiveCharacterTextSplitter:
    """
    Create and return a RecursiveCharacterTextSplitter.

    Args:
        chunk_size: Maximum number of characters per chunk.
        chunk_overlap: Number of overlapping characters between chunks.
        separators: Custom separators for recursive splitting.

    Returns:
        Configured RecursiveCharacterTextSplitter instance.
    """

    if separators is None:
        separators = [
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            ";",
            ",",
            " ",
            ""
        ]

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=separators,
        keep_separator=True,
        is_separator_regex=False,
        length_function=len,
    )