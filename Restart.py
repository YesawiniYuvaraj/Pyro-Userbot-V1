import sys
import os

def restart_program():
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        os.execl(python, python, script, *sys.argv[1:])
