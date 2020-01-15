from win32gui import GetWindowText, GetForegroundWindow
import time
import psutil

for i in range(5):
    time.sleep(2)
    print(GetWindowText(GetForegroundWindow()))
    print(GetForegroundWindow())
    ++i


