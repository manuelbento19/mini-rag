import requests
from mini_rag.config import ollama

def ask_to_llm(prompt):
    request = requests.post(f"{ollama["url"]}/api/chat", json={
        "model": ollama["model"],
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    return request.json()["message"]["content"]