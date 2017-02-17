import time
import os
import sys
import datetime
from pygame import mixer
from func import format_time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqls import Base, Tasks
from tabulate import tabulate
from termcolor import cprint, colored
from pyfiglet import Figlet


class Pomodoro(object):
    def __init__(self, task_dur=1500, short_break=300, long_break=3060, sound_state=True):
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
        output = ''
        font = Figlet(font = 'banner3')

        while t:
            for i in range(t, 0, -1):
                output = str(format_time(i))
                output = font.renderText(output)
                sys.stdout.write("\r" + output)
                time.sleep(1)
                sys.stdout.flush()
                os.system('cls')
                t -= 1

    def start(self, title):
        self.title = title
        str(title)
        time_stamp = self.start_time
        dstore = []
        dstore.append(title)
        dstore.append(time_stamp)
        self.insert()
        print(dstore)
        self.cycle_control()

    def cycle_control(self):
        try:
            while True:
                font = Figlet(font = 'doom')
                self.timer(self.task_dur)
                if self.cycle == 3:
                    self.sound = mixer.Sound("l.wav")
                    if self.sound_state:
                        self.sound.play()
                    else:
                        cprint(font.renderText(('\n\Sound alert is off\n')),'green')
                    cprint(font.renderText(('\nTake a long_break\n')),'green')
                    time.sleep(self.long_break)
                    self.cycle = 0
                else:
                    self.sound = mixer.Sound("w.wav")
                    self.play_sound()
                    cprint(font.renderText(('\nTake a short break\n')),'green', attrs=['blink'])
                    time.sleep(self.short_break)
                    self.cycle += 1
        except KeyboardInterrupt:
            self.stop_app(self.title)

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
        except ValueError:
            return 'Please provide numeric value for config'

        msg = "Hi Configurations are as follows:"
        msg += "\nTask Time: " + str(self.task_dur)
        msg += "\nPomodoro Short Break: " + str(self.short_break)
        msg += "\nPomodoro Long Break: " + str(self.long_break)
        msg += "\nPomodoro Sound Status: " + str(self.sound_state)
        cprint((msg), 'green')

    def stop_app(self, title):
        font = Figlet(font = 'doom')
        self.stop = True
        cprint(font.renderText('\n' + title + '  Is completed'),'yellow')

    def insert(self):
        engine = create_engine("sqlite:///tasklist.db")
        Base.metadata.bind = engine
        dbession = sessionmaker(bind=engine)
        session = dbession()

        new_task = Tasks()
        new_task.task_name = self.title
        new_task.day = self.start_time
        new_task.stop_time = time.ctime()
        session.add(new_task)
        session.commit()

    def query(self):
        engine = create_engine("sqlite:///tasklist.db")
        Base.metadata.bind = engine
        dbession = sessionmaker()
        dbession.bind = engine
        session = dbession()
        print('\n'+ tabulate({
                        'Start-Time': [str(x[0]) for x in session.query(Tasks.day).all()],
                        'Stop-Time': [str(x[0]) for x in session.query(Tasks.stop_time).all()],
                        'Names': [str(x[0]) for x in session.query(Tasks.task_name).all()]
                        }, headers="keys",
                       tablefmt="fancy_grid") + '\n')
