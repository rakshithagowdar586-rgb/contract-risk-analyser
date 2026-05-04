import hashlib

def generate_key(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()