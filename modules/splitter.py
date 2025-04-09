def split_into_chunks(text: str, max_chars: int = 2000) -> list:
    paragraphs = text.split("\n")
    chunks, current = [], ""
    for p in paragraphs:
        if len(current + p) > max_chars:
            chunks.append(current.strip())
            current = p
        else:
            current += "\n" + p
    if current:
        chunks.append(current.strip())
    return chunks