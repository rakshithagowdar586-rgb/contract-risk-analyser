import hashlib
import json

# SIMPLE IN-MEMORY CACHE (fallback instead of Redis)
cache_store = {}

TTL = 60 * 15  # 15 min (not actually enforced in simple mode)


# services/cache_service.py

def get_cache(key):
    return None

def set_cache(key, value):
    return None