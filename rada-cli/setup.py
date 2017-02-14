"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from pomodoro import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""

    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=pomodoro', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'pomodoro',
    version = __version__,
    description = 'A skeleton command line program in Python.',
    long_description = long_description,
    url = 'https://github.com/ProberI/bc-15-pomodoro_Rada',
    author = 'Paul Upendo',
    author_email = 'lovepaul46@outlook.com',
    license = 'UNLICENSE',
    classifiers = [

    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'pomodoro=pomodoro.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
