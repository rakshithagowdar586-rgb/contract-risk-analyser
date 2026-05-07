import time

_request_times = []
_start_time = time.time()

def add_request_time(t):
    try:
        _request_times.append(float(t))
    except:
        pass

def get_metrics():
    if not _request_times:
        return {
            "requests_tracked": 0,
            "avg_response_time_sec": 0
        }

    avg = sum(_request_times) / len(_request_times)

    return {
        "requests_tracked": len(_request_times),
        "avg_response_time_sec": round(avg, 4)
    }

def get_uptime():
    return round(time.time() - _start_time, 2)

def load_model():
    print("Loading sentence-transformers model...")