from random import randint

pfc = dict()
pfc[0] = "pierre"
pfc[1] = "feuille"
pfc[2] = "ciseaux"


n = int(input())

for i in range(n):
    last_adv, has_win = input()
    print(randint(0,2))
