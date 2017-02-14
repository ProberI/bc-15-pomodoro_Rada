from datetime import datetime
from os import system
import time

class Pomo(object):
    time_val = []

    def __init__(self, short_break=5, task_dur=25, long_break=15, sound=True, title=''):
        self.short_break = short_break
        self.task_dur = task_dur
        self.long_break = long_break
        self.sound = sound
        self.day_today = datetime.now().strftime('%H'+':'+'%M'+':'+'%S')
        self.time_val = [self.day_today]
        self.stop = False
        self.title = title
        print self.time_val

    def timer(self, minutes):
        while minutes:
            if self.stop is True:
                break
            mins, secs = divmod(minutes, 60)
            display_format = '{:02d}:{:02d}'.format(mins, secs)
            clear()
            print 'task:' + self.title
            time.sleep(1)
            minutes -= 1


def clear():
        system('Clear')

Pomo()












