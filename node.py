import subprocess


def check_node_installation():
    result = subprocess.call(['node', '-v'], stderr=subprocess.STDOUT)



def run():
    check_node_installation()
