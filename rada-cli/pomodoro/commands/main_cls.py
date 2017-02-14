import datetime


class Pomo(object):
    def __init__(self, shortbreak=5, task_dur=25, long_break=15, sound=True ):
        self.shortbreak = shortbreak
        self.task_dur = task_dur
        self.long_break = long_break
        self.sound = sound


