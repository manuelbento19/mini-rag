
from pathlib import Path

def chunk_files(docs_dir: str = "docs") -> list[dict]:
    chunks = []

    docs_path = Path(docs_dir)

    for file_path in sorted(docs_path.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")

        paragraphs = content.split("\n\n")

        for index, paragraph in enumerate(paragraphs):
            text = paragraph.strip()

            if not text:
                continue

            chunks.append({
                "content": text,
                "source": file_path.name,
                "chunk_id": index
            })

    return chunks
