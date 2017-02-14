"""
pomodoro

Usage:
   pomodoro start
   pomodoro config time
   pomodoro short_break
   pomodoro long_break
   pmodoro sound
   pomodoro stop
   pomodoro list

Options:
    -h --help                   Show this screen
    --version                   Show this version

"""

from inspect import getmembers, isclass


from docopt import docopt

def main():
    """Main CLI entrypoint"""
    import commands
    options = docopt(__doc__, __version__)