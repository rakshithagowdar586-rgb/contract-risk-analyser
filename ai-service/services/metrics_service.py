import time
from threading import Lock

# Thread-safe storage
_request_times = []
_lock = Lock()

# Track when service started
_start_time = time.time()


def add_request_time(response_time):
    """Add a response time entry (thread-safe)"""
    with _lock:
        _request_times.append(response_time)


def get_metrics():
    """Return calculated metrics"""
    with _lock:
        count = len(_request_times)
        avg = sum(_request_times) / count if count > 0 else 0

    return {
        "avg_response_time_sec": round(avg, 4),
        "requests_tracked": count
    }


def get_uptime():
    """Return uptime in seconds"""
    return round(time.time() - _start_time, 2)