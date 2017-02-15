#!/usr/bin/venv python
# -*-coding: utf-8 -*-

"""
Usage:
    pomodoro start <task-title>
    pomodoro list <date>
    pomodoro list_all
    pomodoro config short_break | long_break | sound
    pomodoro clear
    pomodoro (-i | --interactive)
    pomodoro (-h | --help | --version)
    pomodoro exit

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.


"""


import sys
import cmd
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


class Rada_CLI (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'pomodoro -->'
    file = None

    @docopt_cmd
    def do_start(self, arg):
        """ Usage: start <task-title> """
        task = arg['<task-title>']
        '''duration = int(arg['--duration'])
        short_break = int(arg['--short_break'])
        long_break = int(arg['--long_break'])
        rada.start(task, duration, short_break, long_break)'''
        rada.start(task)
        print(arg)


    @docopt_cmd
    def do_config_time(self, arg):
        """ Usage: config_time <duration-in-minutes> """
        rada.config_app(task_dur=arg['<duration-in-minutes>'])



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    rada = Pomodoro()
    Rada_CLI().cmdloop()


print(opt)

