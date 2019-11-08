import time
import threading
import datetime
import sys


class Clock(threading.Thread):
    def __init__(self):
        self._start = None
        self.str_time = None
        self.cur_game_time_dic = None
        threading.Thread.__init__(self)



    #Want 50 years in 2 hours
    YEAR_IN_SECONDS = 31536000
    GAME_DURATION = 50  # years
    FULL_SECOND_DURATION = YEAR_IN_SECONDS * GAME_DURATION
    TWO_HOURS = 7200
    MULTIPLIER = FULL_SECOND_DURATION / TWO_HOURS

    #Default epoch is 1970 but we need to start in 1947
    #Need to offset by 23 years
    OFFSET = 725328000

    YEAR_ZERO = datetime.datetime(1970, 1, 1)
    YEAR_OFFSET = datetime.timedelta(seconds=-OFFSET)

    def run(self):
        self._start = time.time()

        while True:
            time_passed = time.time() - self._start

            game_time_passed = Clock.MULTIPLIER * time_passed

            cur_time = Clock.YEAR_ZERO + Clock.YEAR_OFFSET + datetime.timedelta(seconds=game_time_passed)
            self.cur_game_time_dic = {"year": cur_time.year,
                                      "month": cur_time.month,
                                      "day": cur_time.day,
                                      "hour": cur_time.hour}

            self.str_time = cur_time.strftime("%m/%d/%Y, %H:%M:%S")

            print('\b\b\b\b\b' + cur_time.strftime("%m/%d/%Y, %H:%M:%S"), end='')
            # print(time_passed)
            sys.stdout.flush()
            time.sleep(0.1)
