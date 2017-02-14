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

from inspect import getmembers, isclass

from docopt import docopt

def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()


