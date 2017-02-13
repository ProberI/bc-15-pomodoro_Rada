from codecs import open
from subprocess import call
from os.path import abspath, dirname, join
from setuptools import setup

from pomodoro import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

class RunTests(Command):
    """Run all Tests"""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests"""
        termErr = call(['py.test', '--cov=Rada', '--cov-report=term-missing'])
        raise SystemExit(termErr)

setup(
    name="Pomodoro_Rada",
    version=__version__,
    entry_points={'console_scripts': ['Rada=Rada.cli:main', ], },
    description="",
    long_description=long_description,
    url="",
    author="Paul Upendo",
    authorEmail="lovepaul46@outlook.com",
    LICENSE="UNLICENSED",
    classifiers=[""],
    install_requires=['docopt'],
    packages=find_packages(exclude=['docs', 'venv', 'tests*'])
)


