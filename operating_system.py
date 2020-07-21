from constants import operating_systems
import platform

class operating_system:
    type


def check_operating_system():
    os = platform.system()
    print('Your operating system is ', end='')
    if os == operating_systems.WINDOWS:
        print(operating_systems.WINDOWS)
    elif os == operating_systems.LINUX:
        print(operating_systems.LINUX)
    else:
        print(operating_systems.MAC)


def run():
    check_operating_system()