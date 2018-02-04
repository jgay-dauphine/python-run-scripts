#!/usr/bin/python

# -*- coding: utf8 -*-

import subprocess

def send_message(pipe, message):
    pipe.write(message)
    pipe.write('\n')
    pipe.flush()

def read_message(pipe):
    return pipe.readline().strip()

# Nombre d'iterations...
nb = 50000

pfc = dict()
pfc[0] = "pierre"
pfc[1] = "feuille"
pfc[2] = "ciseaux"

winner = dict()
winner["0,1"] = "j2"
winner["0,2"] = "j1"
winner["1,0"] = "j1"
winner["1,2"] = "j2"
winner["2,0"] = "j2"
winner["2,1"] = "j1"

j1 = subprocess.Popen(['python', '-u', 'ai_stupide.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
j2 = subprocess.Popen(['python', '-u', 'ai_proba.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

send_message(j1.stdin, str(nb))
send_message(j2.stdin, str(nb))

victoires = []
vj1 = 0
vj2 = 0
lj1 = -1
lj2 = -1

for i in range(nb):
    m = str(lj2) + "," + str(vj1)
    send_message(j1.stdin, m)
    m = str(lj1) + "," + str(vj2)
    send_message(j2.stdin, m)

    lj1 = int(read_message(j1.stdout))
    lj2 = int(read_message(j2.stdout))

    if( lj1 == lj2 ):
        vj1 = 0
        vj2 = 0
        # print("Egalite sur cette manche : " + pfc[lj1])
        victoires.append(0)
    elif( winner[str(lj1)+","+str(lj2)] == "j1"):
        vj1 = 1
        vj2 = -1
        # print("Le joueur 1 gagne cette manche : " + pfc[lj1])
        victoires.append(1)
    elif( winner[str(lj1)+","+str(lj2)] == "j2"):
        vj1 = -1
        vj2 = 1
        # print("Le joueur 2 gagne cette manche : " + pfc[lj2])
        victoires.append(2)

j1.stdin.close()
j1.stdout.close()
j1.terminate()

j2.stdin.close()
j2.stdout.close()
j2.terminate()

print("Resume :")
vj1 = sum(1 for i in victoires if i == 1)
print("Victoires J1 : " + str(vj1))
vj2 = sum(1 for i in victoires if i == 2)
print("Victoires J2 : " + str(vj2))
vj2 = sum(1 for i in victoires if i == 0)
print("Egalites : " + str(vj2))
