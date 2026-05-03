import hashlib
import json

# SIMPLE IN-MEMORY CACHE (fallback instead of Redis)
cache_store = {}

TTL = 60 * 15  # 15 min (not actually enforced in simple mode)


def generate_key(text: str):
    return hashlib.sha256(text.encode()).hexdigest()


def get_cache(key):
    return cache_store.get(key)


def set_cache(key, value):
    cache_store[key] = value