
from typing import Sequence

import numpy as np
import requests

from mini_rag.config import embed as embed_config


def embed_text(texts: str | Sequence[str]) -> np.ndarray:
    if isinstance(texts, str):
        texts = [texts]

    if not texts or not all(text.strip() for text in texts):
        raise ValueError("Texts can not be empty.")

    url = f'{embed_config["url"]}/api/embed'

    payload = {
        "model": embed_config["model"],
        "input": list(texts)
    }

    response = requests.post(
        url,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    embeddings = response.json()["embeddings"]

    return np.asarray(embeddings, dtype=np.float32)
