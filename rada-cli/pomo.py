import time
from pygame import mixer
from func import format_time


class Pomodoro(object):
    def __init__(self, task_dur=10, short_break=5, long_break=10, sound_state=True):
        self.task_dur = task_dur
        self.sound_state = sound_state
        self.short_break = short_break
        self.long_break = long_break
        self.cycle = 0
        self.start_time = time.ctime()
        self.stop = False
        mixer.init()
        self.sound = mixer.Sound("w.wav")

    def play_sound(self):
        if self.sound_state:
            self.sound.play()
        else:
            print('Sound alert off')

    def timer(self, t):

        while t:
            for i in range(t, 0, -1):
                time.sleep(1)
                print(format_time(i))
                t -= 1

    '''def start(self, title, duration = None, short_break = None, long_break = None):'''

    def start(self, title):
        """self.task_dur = duration
        self.short_break = short_break
        self.long_break = long_break"""
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
                self.sound = mixer.Sound("l.wav")
                if self.sound_state:
                    self.sound.play()
                else:
                    print('Sound alert is off')
                print('Take a long_break')
                time.sleep(self.long_break)
                self.cycle = 0
            else:
                self.sound = mixer.Sound("w.wav")

                self.play_sound()
                print('Take a short break')
                time.sleep(self.short_break)
                self.cycle += 1

    def config_app(self, **kwargs):
        try:
            for key in kwargs:
                if key == 'task_dur':
                    self.task_dur = int(kwargs[key])
                elif key == 'short_break':
                    self.short_break = int(kwargs[key])
                elif key == 'long_break':
                    self.long_break = int(kwargs[key])
                elif key == 'sound_state':
                    if kwargs[key] == 'True' or kwargs[key] == 'true':
                        self.sound_state = True
                    elif kwargs[key] == 'False' or kwargs[key] == 'false':
                        self.sound_state = False
        except:
            return 'Please provide numeric value for config'

    def stop_app(self):
        self.stop = True
        print(self.title + ' Is completed')
