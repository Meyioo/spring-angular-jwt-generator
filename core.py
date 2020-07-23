import re
import subprocess


def check_installation(command, name):
    result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found ' + name + ' installation version:\t', match.group(0))
    else:
        print('Version not found. Please install the latest version of ' + name + ' on your System.')
