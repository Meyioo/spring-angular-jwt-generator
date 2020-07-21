import subprocess
import re


def check_maven_installation():
    result = subprocess.check_output(['mvn', '-v'], stderr=subprocess.STDOUT)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found Maven installation version:', match.group(0))
    else:
        print('Version not found. Please install the latest version of Maven on your System.')
        choice = input('Install the latest maven version Y/N?: ')
        if choice == 'Y':
            setup()


def setup():
    x = 0

def run():
    check_maven_installation()
