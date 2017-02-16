#!/usr/bin/venv python
# -*-coding: utf-8 -*-

"""
Usage:
    pomodoro start <task-title>
    pomodoro list <date>
    pomodoro list_all
    pomodoro config_ short_break | long_break | sound
    pomodoro clear
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
    pomodoro exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import os
import sys
import cmd
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
from pomo import Pomodoro



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def app_header():
    '''
        This function creates the header that is displayed when the app
        launches
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    cprint(figlet_format('RADA', font='3-d'), 'white')
    cprint('====================================================', 'blue')
    cprint("\tRada implements pomodoro technique.", 'yellow')
    cprint('====================================================', 'blue')


def custom_print(arg, color='green'):
    ''' This is a simple print function that adds color to printed output. '''
    cprint("\n" + arg + "\n", color)


class Rada_CLI(cmd.Cmd):
    intro = 'Welcome to my interactive pomodoro timer!\n' \
            + ' (type help for a list of commands.)'
    prompt = 'pomodoro->> '
    file = None

    @docopt_cmd
    def do_start(self, arg):
        """ Usage: start <task-title> """
        task = arg['<task-title>']
        rada.start(task)
        print(arg)

    @docopt_cmd
    def do_config_time(self, arg):
        """ Usage: config_time <duration-in-minutes> """
        rada.config_app(task_dur=arg['<duration-in-minutes>'])

    @docopt_cmd
    def do_config_short_break(self, arg):
        """Usage: config_short_break <desired-duration>"""
        rada.config_app(short_break=arg['<desired-duration>'])

    @docopt_cmd
    def do_config_long_break(self, arg):
        """Usage: config_long_break <desired-duration>"""
        rada.config_app(long_break=arg['<desired-duration>'])

    @docopt_cmd
    def do_config_sound(self, arg):
        """Usage: config_sound <True-False>"""
        rada.config_app(sound_state=arg['<True-False>'])

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list"""
        rada.query()

    def do_stop(self, arg):
        """Usage stop <task-title>"""
        rada.stop_app(arg)



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    app_header()
    rada = Pomodoro()
    Rada_CLI().cmdloop()

print(opt)
