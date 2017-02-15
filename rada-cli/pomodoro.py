from os import system
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



    def timer(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat,end='\t')
           # print('task' +self.title)
            time.sleep(1)
            t -= 1


    def pomo_control(self):
        while not self.stop:
            # self.timer(self.task_dur)

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
                    self.timer(self.long_break)
                    self.cycles = 0
                    print('third Cycle' + str(duration))
                else:
                    self.timer(self.short_break)
                    self.cycles += 1
            except KeyboardInterrupt:
                print('Interrupting')
    def config_app(self, **args):
        try:
            for key in args:
                if key == 'task_time':
                    self.task_dur = int(args[key])
                elif key == 'short_break':
                    self.short_break = int(args[key])
                elif key == 'long_break':
                    self.long_break = int(args[key])

        except TypeError:
            return 'Please allocate time as number'

    def stop(self):
        self.stop = True







Pomo().timer(25)