import core
from constants import constants


def check_java_installation():
    core.check_installation(constants.COMMAND_JAVA, 'Java')


def run():
    check_java_installation()
