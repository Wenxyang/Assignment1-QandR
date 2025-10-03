from openai import OpenAI

def validate_api_key(key: str) -> bool:
    try:
        client = OpenAI(api_key=key)
        client.embeddings.create(model="text-embedding-3-small", input="ping")
        return True
    except Exception:
        return False
