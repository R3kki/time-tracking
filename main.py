from win32gui import GetWindowText, GetForegroundWindow
import time
import re
import psutil

TIME_INTERVAL = 2
RUNNING = 1
DAILY = 86400

data = {}


def collect_data(duration):
    prev_program = ''
    timeout = duration
    if duration <= 0:
        timeout = DAILY
    for i in range(timeout):
        time.sleep(TIME_INTERVAL)
        raw_window_info = GetWindowText(GetForegroundWindow())
        curr_program = (re.split(' - ', raw_window_info))[-1]
        if prev_program in data:
            data[prev_program] += TIME_INTERVAL
        elif prev_program != '':
            data[prev_program] = TIME_INTERVAL
        prev_program = curr_program
        ++i
        print(data)


# test with 6 seconds of running
collect_data(6)



