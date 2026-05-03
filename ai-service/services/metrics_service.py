import time

_start_time = time.time()
response_times = []


# start request timer
def start_timer():
    return time.time()


# end request timer + store duration
def end_timer(start):
    duration = time.time() - start
    response_times.append(duration)
    return duration


# average response time
def get_avg_response_time():
    if not response_times:
        return 0
    return sum(response_times) / len(response_times)


# uptime of server
def get_uptime():
    return time.time() - _start_time