import core
from constants import constants


def check_maven_installation():
    core.check_installation(constants.COMMAND_MAVEN, 'Maven')


def run():
    check_maven_installation()
