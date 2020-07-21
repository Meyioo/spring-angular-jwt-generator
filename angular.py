import re
import subprocess


def check_angular_installation():
    result = subprocess.check_output(['ng', 'version'], stderr=subprocess.STDOUT)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found angular installation version:', match.group(0))
    else:
        print('Version not found. Please install the latest version of angular cli on your System.')


def run():
    check_angular_installation()
