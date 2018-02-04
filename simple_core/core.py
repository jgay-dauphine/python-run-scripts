#!/usr/bin/python

# -*- coding: utf8 -*-

import subprocess

def send_message(pipe, message):
    print("writing to subprocess: " + message)
    pipe.write(message)
    pipe.write('\n')
    pipe.flush()

def read_message(pipe):
    return pipe.readline().strip()

# Nombre d'iterations...
nb = 5

child = subprocess.Popen(['python', '-u', 'ai.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

send_message(child.stdin, str(nb))

for i in range(nb):
    send_message(child.stdin, str(i))
    ret = int(read_message(child.stdout))
    print("reading from subprocess: " + str(ret))

child.stdin.close()
child.stdout.close()
