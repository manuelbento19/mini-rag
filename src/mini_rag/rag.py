
from mini_rag.llm import ask_to_llm
from mini_rag.embed import embed_text
from mini_rag.chunk import chunk_files

import numpy as np


chunks = chunk_files()

if not chunks:
    raise ValueError("No documents found to index.")

texts = [chunk["content"] for chunk in chunks]

vector_chunks = embed_text(texts)

def retrieve(question: str, top: int = 3) -> list[dict]:
    if not question.strip():
        return []

    if top <= 0:
        raise ValueError("'top' must be greater than zero.")

    question_vector = embed_text([question])[0]

    numerator = vector_chunks @ question_vector

    denominator = ( np.linalg.norm(vector_chunks, axis=1) * np.linalg.norm(question_vector))

    scores = np.divide(
        numerator,
        denominator,
        out=np.zeros_like(numerator, dtype=float),
        where=denominator != 0
    )

    top_indices = np.argsort(scores)[::-1][:top]

    return [chunks[i] for i in top_indices]

def rag(question: str) -> str:
    context_chunks = retrieve(question)

    context = "\n\n".join(
        f"Source: {chunk['source']}\n{chunk['content']}"
        for chunk in context_chunks
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

while True:
    question = input("Ask: ").strip()

    if question.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    if not question:
        continue

    answer = rag(question)

    print(f"\n{answer}\n")
