from subprocess import call
import time

def add(filename=None):
    if filename:
        call(['git', 'add', filename])
    else:
        call(['git', 'add', '-A'])

def commit():
    call(['git','commit','-m','%d' % int(time.time())])

def push(branch=None):
    if branch:
        call(['git','push','origin','master'])
    else:
        call(['git','push'])

def pull():
    call(['git','pull'])

    
