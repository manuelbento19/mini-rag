import numpy as np

from mini_rag.chunk import chunk_files
from mini_rag.embed import embed_text
from mini_rag.llm import ask_to_llm


class RAG:
    def __init__(self, chunks: list[dict], vectors: np.ndarray) -> None:
        self.chunks = chunks
        self.vectors = vectors

    @classmethod
    def from_docs(cls, docs_dir: str = "docs") -> "RAG":
        chunks = chunk_files(docs_dir)

        if not chunks:
            raise ValueError("No documents found to index.")

        texts = [chunk["content"] for chunk in chunks]
        vectors = embed_text(texts)

        return cls(chunks, vectors)

    def retrieve(self, question: str, top: int = 3) -> list[dict]:
        if not question.strip():
            return []

        if top <= 0:
            raise ValueError("'top' must be greater than zero.")

        question_vector = embed_text([question])[0]

        numerator = self.vectors @ question_vector
        denominator = np.linalg.norm(self.vectors, axis=1) * np.linalg.norm(question_vector)
        scores = np.divide(
            numerator,
            denominator,
            out=np.zeros_like(numerator, dtype=float),
            where=denominator != 0,
        )

        top_indices = np.argsort(scores)[::-1][:top]
        return [self.chunks[i] for i in top_indices]

    def ask(self, question: str) -> str:
        context = "\n\n".join(
            f"Source: {chunk['source']}\n{chunk['content']}"
            for chunk in self.retrieve(question)
        )

        prompt = f"""
        Answer the question using ONLY the context below.

        If the answer is not available in the context,
        say "I don't know".

        Context:
        {context}

        Question:
        {question}
        """

        return ask_to_llm(prompt)


def build_rag(docs_dir: str = "docs") -> RAG:
    return RAG.from_docs(docs_dir)
