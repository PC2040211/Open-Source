import os.path
from os import path
import json
import requests;
import time
import sys
from colorama import *
import subprocess
import sys
import os
from colored import fg

yellow = fg('yellow')
red = fg('red')

def banner1():
    animation = "|/-\\"
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
banner1()

def banner2():
    print('''
    %s     ______  __  __  __  __       __  __%s
    %s    / ____/ / / / / / / / /      / / / /%s     %s-------------------------%s
    %s   / /__   / / / / / /_/ /      / / / / %s     %sCreated by:              %s
    %s  / ___/  / / / / / _  _/      / / / /  %s     %s           DELLUCIFER    %s
    %s / /     / /_/ / / / \ \      / /_/ /   %s     %s-------------------------%s
    %s/_/      \____/ /_/   \_\     \____/    %s
    
    ''' % (yellow, yellow, red, yellow, red, yellow, red, yellow, red, yellow))

banner2()