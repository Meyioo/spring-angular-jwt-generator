import re
import subprocess


def check_java_installation():
    result = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    match = re.search(r"\d+\.\d+\.\d", str(result))
    if match is not None:
        print('Found java installation version:', match.group(0))
    else:
        print('Version not found!')


check_java_installation()