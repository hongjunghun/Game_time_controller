import time
import os

class Timing():
    def __init__(self):
        pass

    def input_wanting_time(self, h, m, s, file):
        print(f"{h:02}시 {m:02}분 {s:02}초에 {file}을(를) 종료합니다.")

        now = time.localtime()
        current_total = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
        target_total = h * 3600 + m * 60 + s
        delay = target_total - current_total

        if delay > 0:
            time.sleep(delay)

        result = os.system(f"taskkill /im {file} /f")
        if result != 0:
            print(f"{file} 종료에 실패했습니다. 관리자 권한이 필요할 수 있습니다.")