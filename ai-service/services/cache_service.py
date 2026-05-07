# Simple in-memory cache with optional TTL support

import time

# ----------------------------
# CACHE STORAGE
# ----------------------------
_cache = {}

# Structure:
# _cache[key] = {
#     "value": <data>,
#     "expiry": <timestamp or None>
# }


# ----------------------------
# SET CACHE
# ----------------------------
def set_cache(key, value, ttl=None):
    """
    Store value in cache

    Args:
        key (str): cache key
        value (any): data to store
        ttl (int, optional): time-to-live in seconds
    """
    expiry = time.time() + ttl if ttl else None

    _cache[key] = {
        "value": value,
        "expiry": expiry
    }


# ----------------------------
# GET CACHE
# ----------------------------
def get_cache(key):
    """
    Retrieve value from cache

    Returns:
        value if exists and not expired
        None otherwise
    """
    item = _cache.get(key)

    if not item:
        return None

    # Check expiry
    if item["expiry"] and time.time() > item["expiry"]:
        del _cache[key]
        return None

    return item["value"]


# ----------------------------
# DELETE CACHE
# ----------------------------
def delete_cache(key):
    """
    Remove key from cache
    """
    if key in _cache:
        del _cache[key]


# ----------------------------
# CLEAR ALL CACHE
# ----------------------------
def clear_cache():
    """
    Clear entire cache
    """
    _cache.clear()


# ----------------------------
# DEBUG (OPTIONAL)
# ----------------------------
def get_cache_size():
    """
    Returns number of cached items
    """
    return len(_cache)