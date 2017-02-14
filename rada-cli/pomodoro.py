import time

class Pomo(object):
    time_val = []

    def __init__(self, short_break=5, task_dur=25, long_break=15, title=''):
        self.short_break = short_break
        self.task_dur = task_dur
        self.long_break = long_break
        self.title = title
        self.start_time = time.ctime()
        self.cycles = 0
        self.stop = False

    def start(self, title):
        self.title = title
        print(title + "\tStart Time : %s" % self.start_time)
        self.stop = False
        self.pomo_control()



    def timer(self, duration):
        try:
            print(self.start_time + 'work now')
            duration = self.task_dur
            int(duration) * 60
            time.sleep(duration)
            print(self.start_time + 'rest now')
            duration = self.short_break
            int(duration) * 60
            time.sleep(duration)
            print(self.start_time + 'Cycle complete')
            if self.cycles == 3:
                print('third Cycle' + duration)

        except KeyboardInterrupt:
            print('Interrupting')


    def pomo_control(self):
        while not self.stop:
            self.timer(self.task_dur)
            if self.cycles == 3:
                self.timer(self.long_break)
                self.cycles = 0
            else:
                self.timer(self.short_break)
                self.cycles += 1






















