import time
import sys
from pygame import mixer
from func import format_time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqls import Base, Tasks
from tabulate import tabulate


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
                sys.stdout.write("\r %s" % format_time(i))
                sys.stdout.flush()
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
        self.insert()
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
                    print('\tSound alert is off')
                print('\tTake a long_break')
                time.sleep(self.long_break)
                self.cycle = 0
            else:
                self.sound = mixer.Sound("w.wav")

                self.play_sound()
                print('\tTake a short break')
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

    def insert(self):
        engine = create_engine("sqlite:///tasklist.db")
        Base.metadata.bind = engine
        dbession = sessionmaker(bind=engine)
        session = dbession()

        new_task = Tasks()
        new_task.task_name = self.title
        new_task.day = self.start_time
        session.add(new_task)
        session.commit()

    def query(self):
        engine = create_engine("sqlite:///tasklist.db")
        Base.metadata.bind = engine
        dbession = sessionmaker()
        dbession.bind = engine
        session = dbession()
        print(tabulate({'Names':session.query(Tasks.task_name).all(), 'Time': session.query(Tasks.day).all()}, headers="keys", tablefmt="fancy_grid"))






