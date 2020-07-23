from constants import constants
import platform


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
