import re
import subprocess
import platform
from constants import constants


def check_installation(command, name):
    result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found ' + name + ' installation version:\t', match.group(0))
    else:
        print('Version not found. Please install the latest version of ' + name + ' on your System.')


def check_operating_system():
    os = platform.system()
    print('Your operating system is ', end='')
    if os == constants.WINDOWS:
        print(constants.WINDOWS)
    elif os == constants.LINUX:
        print(constants.LINUX)
    else:
        print(constants.MAC)


def run():
    check_operating_system()
    check_installation(constants.COMMAND_JAVA, 'Java')
    check_installation(constants.COMMAND_MAVEN, 'Maven')
    check_installation(constants.COMMAND_NODE, 'Node')
    check_installation(constants.COMMAND_NG, 'Angular')
