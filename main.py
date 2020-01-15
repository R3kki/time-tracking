from win32gui import GetWindowText, GetForegroundWindow
import time
import re
import psutil

TIME_INTERVAL = 2
RUNNING = 1
DAILY = 86400


def collect_data(duration):
    collected_data = {}
    prev_program = ''
    timeout = duration
    if duration <= 0:
        timeout = DAILY
    for i in range(timeout):
        time.sleep(TIME_INTERVAL)
        raw_window_info = GetWindowText(GetForegroundWindow())
        curr_program = (re.split(' - ', raw_window_info))[-1]
        if prev_program in collected_data:
            collected_data[prev_program] += TIME_INTERVAL
        elif prev_program != '':
            collected_data[prev_program] = TIME_INTERVAL
        prev_program = curr_program
        ++i
    return collected_data


# test with 6 seconds of running

data = collect_data(6)
print(data)
