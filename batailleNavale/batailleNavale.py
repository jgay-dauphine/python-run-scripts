# -*- coding: utf-8 -*-

"""
Bataille Navale

Script de jeu de bataille navale pour
deux joueurs

Created on Fri Jan 26 15:40:45 2018
"""

import os
import platform

def clean():
    mon_os = platform.system()
    commands = dict()
    commands["Linux"] = "clear"
    commands["Windows"] = "cls"
    commands["Darwin"] = "clear"
    os.system(commands[mon_os])
    # print("\n" * 100)

# Création d'un dictionnaire pour convertir en A en 0, B en 1...
alpha = "abcdefghijklmnopqrstuvwxyz".upper()


# Humm.. ToDo : change this !
convertir = dict()
cpt_convertir = 0
for i in alpha:
    convertir[i] = cpt_convertir
    cpt_convertir = cpt_convertir +1


def display_grille(game, isJoueur1):
    if isJoueur1:
        g1 = game["grille_p1"]
        g2 = game["grille_p1_p2"]
    else:
        g1 = game["grille_p2"]
        g2 = game["grille_p2_p1"]

    alpha = "abcdefghijklmnopqrstuvwxyz"

    if game["size_x"] < 10 :
        print(" ", alpha[:game["size_x"] ].upper(), "    ", alpha[:game["size_x"] ].upper())
    else :
        print("  ", alpha[:game["size_x"] ].upper(), "    ", alpha[:game["size_x"] ].upper())
    
    cpt = 1
    display_g1 = [[ game["signes"][i] for i in line ] for line in g1 ]
    display_g2 = [[ game["signes"][i] for i in line ] for line in g2 ]
    for cpt in range(game["size_y"]):
        if game["size_x"] < 10 :
            print(str(cpt+1), ''.join(display_g1[cpt]),'  ', str(cpt+1), ''.join(display_g2[cpt]))
        else :
            if cpt < 9:
                print('',str(cpt+1), ''.join(display_g1[cpt]),'  ', str(cpt+1), ''.join(display_g2[cpt]))
            else :
                print(str(cpt+1), ''.join(display_g1[cpt]),' ', str(cpt+1), ''.join(display_g2[cpt]))

# Rang 5

def verif_case(game, grille, taille, coordonnees, inclinaison):
    case_vide = True
    
    if inclinaison == "v":
        if coordonnees[0] > game["size_x"] - game["navires"][taille]["taille"]:
            case_vide = False
    else:
        if coordonnees[1] > game["size_x"] - game["navires"][taille]["taille"]:
            case_vide = False
        
    if case_vide:
        if inclinaison == "v":
            for nb_cases in range(game["navires"][taille]["taille"]):
                if grille[coordonnees[0]+nb_cases][coordonnees[1]]!=0:
                    case_vide = False
        if inclinaison == "h":
            for nb_cases in range(game["navires"][taille]["taille"]):
                if grille[coordonnees[0]][coordonnees[1]+nb_cases]!=0:
                    case_vide = False
    return case_vide

def place_ships(game, isJoueur1):
    if isJoueur1:
        navires_joueur = game["p1"]
        grille = game["grille_p1"]
    else:
        navires_joueur = game["p2"]
        grille = game["grille_p2"]
    
    print("Bonjour, %s." % ("Joueur 1" if isJoueur1 else "Joueur2"))
    
    display_grille(game, isJoueur1)
    
    cpt = 1
    for taille in game["navires"]:
        cpt_bateau_par_taille = 1
        for nb_navires in range(game["navires"][taille]["nb"]):
            nb_navires += 1
            navires_joueur["navire"+str(cpt)] = dict()
            navires_joueur["navire"+str(cpt)]["coordonnees"] = dict()
            navires_joueur["navire"+str(cpt)]["touche"] = dict()
            
            print "Placez un", taille, "bateau de", game["navires"][taille]["taille"], "cases", "(%s/%s)" % (cpt_bateau_par_taille, game["navires"][taille]["nb"]), ":"
            cpt_bateau_par_taille = cpt_bateau_par_taille + 1
            
            coordonnees = ask_coordinates()
            print "Verical (v) ou horizontal (h) ?"
            inclinaison = raw_input()
            
            while inclinaison != "v" and inclinaison != "h":
                print("Seulement (v) ou (h) svp")
                print "Verical (v) ou horizontal (h) ?"
                inclinaison = raw_input()
                        
            while not(verif_case(game, grille, taille, coordonnees, inclinaison)):
                print("Impossible de placer un bateau ici")
                coordonnees = ask_coordinates()
                print "Verical (v) ou horizontal (h) ?"
                inclinaison = raw_input()
                while inclinaison != "v" and inclinaison != "h":
                    print("Seulement (v) ou (h) svp")
                    
            
            for nb_cases in range(game["navires"][taille]["taille"]):
                if inclinaison == "v":
                    coordonnes_bis = [coordonnees[0]+nb_cases, coordonnees[1]]
                    grille[coordonnes_bis[0]][coordonnes_bis[1]]=1
                    navires_joueur["navire"+str(cpt)]["coordonnees"][str(nb_cases)] = coordonnes_bis
                    navires_joueur["navire"+str(cpt)]["touche"][str(nb_cases)] = 0
                else:
                    coordonnes_bis = [coordonnees[0] , coordonnees[1]+ nb_cases]
                    grille[coordonnes_bis[0]][coordonnes_bis[1]]=1
                    navires_joueur["navire"+str(cpt)]["coordonnees"][str(nb_cases)] = coordonnes_bis
                    navires_joueur["navire"+str(cpt)]["touche"][str(nb_cases)] = 0
                
            display_grille(game, isJoueur1)
            cpt = cpt +1
        

# Rang 4
def ask_coordinates():
    coordonnees="  "
    x=""
    y=0
    print "Choisir les coordonnées ? format A1 : "
    coordonnees = raw_input()
    
    if game["size_y"] < 10:
        try:
            x = coordonnees[0].upper()
            y = int(coordonnees[1])
        except ValueError:
            x = coordonnees[0]
            y = 0
        while len(coordonnees) != 2 or x not in convertir.keys() or y not in range(1,10):
            print("Il faut rentrer une lettre et un chiffre !")
            print "Choisir les coordonnées ? format A1 : "
            coordonnees=raw_input()
            try:
                x = coordonnees[0].upper()
                y = int(coordonnees[1])
            except ValueError:
                x = coordonnees[0]
                y = 0
    else:
        try:
            x = coordonnees[0].upper()
            y = int(coordonnees[1:])
        except ValueError:
            x = coordonnees[0]
            y = coordonnees[1:]
        while (len(coordonnees) != 2 and len(coordonnees) !=3) or x not in convertir.keys() or y not in range(1,game["size_y"]+1):
            print("Il faut rentrer une lettre et un chiffre !")
            print "Choisir les coordonnées ? format A1 : "
            coordonnees=raw_input()
            try:
                x = coordonnees[0].upper()
                y = int(coordonnees[1:])
            except ValueError:
                x = coordonnees[0]
                y = 0
        
    x = int(convertir[x])
    y = y-1
    return (y,x)


# Rang 3
def get_target(game, isJoueur1):
    coord = ask_coordinates()
    verif = True
    if isJoueur1:
        while verif:
            if game["grille_p1_p2"][coord[0]][coord[1]]!=0:
                print('Vous avez deja tapé a cet endroit, ressaisissez')
                coord=ask_coordinates()
            else:
                verif = False
   
        return(coord[0],coord[1])
    else:
        while verif:
            if game["grille_p2_p1"][coord[0]][coord[1]]!=0:
                print('Vous avez deja tapé a cet endroit, ressaisissez')
                coord=ask_coordinates()
            else:
                verif = False
        return(coord[0],coord[1])

# Rang 2

def coule(game, isJoueur1):
    if not(isJoueur1):
        navires_joueur = game["p1"]
        grille1 = game["grille_p1"]
        grille2 = game["grille_p2_p1"]
    else:
        navires_joueur = game["p2"]
        grille1 = game["grille_p2"]
        grille2 = game["grille_p1_p2"]
        
    for bateau in navires_joueur:
        somme = 0
        for touche in navires_joueur[bateau]["touche"]:
            somme = somme + navires_joueur[bateau]["touche"][touche]
        if somme == len(navires_joueur[bateau]["touche"]):
            for coor in navires_joueur[bateau]["coordonnees"]:
                grille1[navires_joueur[bateau]["coordonnees"][coor][0]][navires_joueur[bateau]["coordonnees"][coor][1]] = 4
                grille2[navires_joueur[bateau]["coordonnees"][coor][0]][navires_joueur[bateau]["coordonnees"][coor][1]] = 4
    return(game)
                
def damages(game, isJoueur1, x, y):
    x = int(x)
    y = int(y)
    
    if isJoueur1:
        if game["grille_p2"][x][y]== 1:
            game["grille_p2"][x][y]= 3
            game["grille_p1_p2"][x][y]= 3
            print("Touché")
                
            
        else:
            game["grille_p2"][x][y]= 2
            game["grille_p1_p2"][x][y]= 2
            print("Raté")
            
        for bateau in game["p2"]:
            for coor in range(len(game["p2"][bateau]["coordonnees"])):
                if game["p2"][bateau]["coordonnees"][str(coor)][0] == x and game["p2"][bateau]["coordonnees"][str(coor)][1] == y:
                    game["p2"][bateau]["touche"][str(coor)] = 1

    else:
        if game["grille_p1"][x][y] == 1:
            game["grille_p1"][x][y] = 3
            game["grille_p2_p1"][x][y] = 3
            print("Touché")
            
        else:
            game["grille_p1"][x][y] = 2
            game["grille_p2_p1"][x][y] = 2
            print("Raté")
        
        for bateau in game["p1"]:
            for coor in range(len(game["p1"][bateau]["coordonnees"])):
                if game["p1"][bateau]["coordonnees"][str(coor)][0] == x and game["p1"][bateau]["coordonnees"][str(coor)][1] == y:
                    game["p1"][bateau]["touche"][str(coor)] = 1

    game = coule(game, isJoueur1)
        
    return(game)

# Rang 1



# Création du jeu
game = dict()

game["navires"] = dict()
game["navires"]["grand"] = {"taille": 4, "nb": 1}
game["navires"]["moyen"] = {"taille": 3, "nb": 2}
game["navires"]["petit"] = {"taille": 2, "nb": 2}

# Navires des joueurs :
game["p1"] = dict()
game["p2"] = dict()

# Grilles de n*m cases

print "Nombre de colonnes (pas plus de 26 sinon c'est galère svp) :"
game["size_x"] = raw_input()
try:
    game["size_x"] = int(game["size_x"])
except ValueError:
    game["size_x"] = 0
while game["size_x"] > 26 or game["size_x"] < 1:
    print("Un nombre ...")
    print "Nombre de colonnes (pas plus de 26 sinon c'est galère svp) :"
    game["size_x"] = raw_input()
    try:
        game["size_x"] = int(game["size_x"])
    except ValueError:
        game["size_x"] = 0
    


print "Nombre de lignes (pas plus de 99 sinon c'est galère svp) :"
game["size_y"] = raw_input()
try:
    game["size_y"] = int(game["size_y"])
except ValueError :
    game["size_y"] = 0
while game["size_y"] > 99 or game["size_y"] < 1:
    print("Un nombre ...")
    print "Nombre de lignes (pas plus de 99 sinon c'est galère svp) :"
    game["size_y"] = raw_input()
    try:
        game["size_y"] = int(game["size_y"])
    except ValueError :
        game["size_y"] = 0
    

clean()
    
game["signes"] = { 0:'~', 1:'*', 2:'O', 3:'X', 4:'@'}

# grille pour cacher les bateaux J1
game["grille_p1"] = [ [ 0 for i in range(game["size_x"]) ] for j in range(game["size_y"]) ]
# grille pour cacher les bateaux J2
game["grille_p2"] = [ [ 0 for i in range(game["size_x"]) ] for j in range(game["size_y"]) ]
# grille pour que le J1 tire sur le J2
game["grille_p1_p2"] = [ [ 0 for i in range(game["size_x"]) ] for j in range(game["size_y"]) ]
# grille pour que le J2 tire sur le J1
game["grille_p2_p1"] = [ [ 0 for i in range(game["size_x"]) ] for j in range(game["size_y"]) ]

isJoueur1 = True

# Placement de bâteaux
place_ships(game, True)
clean()


place_ships(game, False)
clean()

print "Joueur 1 tappez entrer pour commencer"
raw_input()
clean()

# Tour de jeu
gameNotEnded = True


while(gameNotEnded):
    # affichage des grilles du joueur
    print("Tour du %s" % ("Joueur 1" if isJoueur1 else "Joueur 2"))
    display_grille(game, isJoueur1)

    # le joueur cible une case
    (x,y) = get_target(game, isJoueur1)
    
    # le joueur a un rapport sur ce qu'il a fait
    game = damages(game, isJoueur1, x, y)
    display_grille(game, isJoueur1)
    
    # Gestion du changement de tour
    
    if isJoueur1:
        if game["grille_p2"] == game["grille_p1_p2"]:
            gameNotEnded = False
            player = 1
            break
    else:
        if game["grille_p1"] == game["grille_p2_p1"]:
            gameNotEnded = False
            player = 2
            break
    
    print("%s tappez entrer pour continuer" % ("Joueur 1" if isJoueur1 else "Joueur 2"))
    raw_input()
    clean()
    
    isJoueur1 = not isJoueur1
    
    print("%s tappez entrer pour continuer" % ("Joueur 1" if isJoueur1 else "Joueur 2"))
    raw_input()
    clean()

    
    
print("Joueur 1 a gagné" if player == 1 else "Joueur 2 a gagné")
