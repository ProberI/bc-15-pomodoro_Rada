from datetime import datetime


class Pomo(object):
    time_val = []

    def __init__(self, short_break=5, task_dur=25, long_break=15, sound=True ):
        self.short_break = short_break
        self.task_dur = task_dur
        self.long_break = long_break
        self.sound = sound
        self.day_today = datetime.now().strftime('%H'+':'+'%M'+':'+'%S')
        self.time_val = [self.day_today]
        print self.time_val








