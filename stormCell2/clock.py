import time
import threading
import datetime
import sys


class Clock(threading.Thread):
    def __init__(self, start_offset=datetime.timedelta(seconds=0)):
        self._start = None
        self.str_time = None
        self.cur_time = None
        self.cur_game_time_dic = None
        self.start_offset = start_offset
        self.should_stop = False
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

    YEAR_MIN = datetime.datetime(1970,1,1)
    YEAR_OFFSET = datetime.timedelta(seconds=-OFFSET)
    YEAR_ZERO = YEAR_MIN + YEAR_OFFSET

    def clone(self):
        return Clock(self.game_time_from_start())

    def stop(self):
        self.should_stop = True

    def game_time_from_start(self):
        return self.cur_time-Clock.YEAR_ZERO

    def game_time_dic(self):
        return {"year": self.cur_time.year,
                "month": self.cur_time.month,
                "day": self.cur_time.day,
                "hour": self.cur_time.hour}

    def game_time_str(self):
        return self.cur_time.strftime("%m/%d/%Y, %H:%M:%S")

    def game_time(self):
        return self.cur_time

    def run(self):
        self._start = time.time()

        while not self.should_stop:
            time_passed = time.time() - self._start

            game_time_passed = Clock.MULTIPLIER * time_passed

            self.cur_time = Clock.YEAR_ZERO + self.start_offset + datetime.timedelta(seconds=game_time_passed)

            print('\b\b\b\b\b' + self.game_time_str(), end='')
            # print(time_passed)
            sys.stdout.flush()
            time.sleep(0.1)
