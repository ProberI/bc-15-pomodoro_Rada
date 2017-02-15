import time

from func import format_time


class Pomodoro(object):
    def __init__(self, task_dur=10, short_break=5, long_break=15):
        self.task_dur = task_dur
        self.short_break = short_break
        self.long_break = long_break
        self.cycle = 0
        self.start_time = time.ctime()
        self.stop = False

    def timer(self, t):
        t = self.task_dur
        while t:
            for i in range(t, 0, -1):
                time.sleep(1)
                print(format_time(i))
                t -= 1

    def start(self, title):
            self.title = title
            str(title)
            time_stamp = self.start_time
            d = []
            d.append(title)
            d.append(time_stamp)
            print(d)
            self.cycle_control()

    def cycle_control(self):
        while not self.stop:
            self.timer(self.task_dur)
            if self.cycle == 3:
                self.timer(self.long_break)
                self.cycle = 0
            else:
                self.timer(self.short_break)
                self.cycle += 1


p = Pomodoro()
p.start('Kanu')
