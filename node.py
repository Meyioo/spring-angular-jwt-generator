import re
import subprocess


def check_node_installation():
    result = subprocess.check_output('cd / | node -v', stderr=subprocess.STDOUT, shell=True)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found node installation version:\t', match.group(0))
    else:
        print('Version not found. Please install the latest version of angular cli on your System.')


def run():
    check_node_installation()
