import requests
from mini_rag.config import ollama

def ask_to_llm(prompt):
    url = f"{ollama["url"]}/api/chat"

    payload = {
        "model": ollama["model"],
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    response = requests.post(
        url,
        json=payload,
    )
    return response.json()["message"]["content"]