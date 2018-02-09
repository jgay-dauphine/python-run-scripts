#!/usr/bin/python

# -*- coding: utf8 -*-

import subprocess
import platform

def send_message(pipe, message):
    pipe.write(message)
    pipe.write('\n')
    pipe.flush()

def read_message(pipe):
    return pipe.readline().strip()

def read_board(game, sx, sy):
    ret = []
    game_output = read_message(game.stdout)
    for i in range(sy):
        game_output = read_message(game.stdout)
        s = game_output.split("'")[-2]
        ret.append([ 0 if c == '~' else 1 if c == 'O' else 2 if c == 'X' else 3 for c in s ])
        print game_output
    print ret
    return ret

def consume_board(game, sx, sy):
    for i in range(sy+1):
        game_output = read_message(game.stdout)

def pause():
    print("Appuyez sur une touche pour continuer...")
    # raw_input()

game = subprocess.Popen(['python', '-u', 'c:\\TP\\batailleNavale.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

j1 = subprocess.Popen(['python', '-u', 'c:\\TP\\ai_stupide.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
j2 = subprocess.Popen(['python', '-u', 'c:\\TP\\ai_debile.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


# Setting up the game
sx = 5
sy = 5
ships = [2,2,3,3,4]

game_output = read_message(game.stdout)
print game_output
send_message(game.stdin, str(sx))
game_output = read_message(game.stdout)
print game_output
send_message(game.stdin, str(sy))

send_message(j1.stdin, str(sx))
send_message(j1.stdin, str(sy))
send_message(j1.stdin, str(ships))
send_message(j2.stdin, str(sx))
send_message(j2.stdin, str(sy))
send_message(j2.stdin, str(ships))


# Read Greetings
game_output = read_message(game.stdout)
# Read Board
read_board(game, sx, sy)
# Place Ships J1
i=0
for size in ships:
    ## Consume inputs
    s = read_message(game.stdout)
    print s
    s = read_message(game.stdout)
    print s
    ## Place each ships
    s = read_message(j1.stdout)
    mess = s
    print 'Sending message :', mess
    send_message(game.stdin, mess)
    s = read_message(game.stdout)
    print s
    s = read_message(j1.stdout)
    mess = s
    print 'Sending message :', mess
    send_message(game.stdin, mess)

    i = i+1
    read_board(game, sx, sy)
    pause()

# Read Greetings
game_output = read_message(game.stdout)
# Read Board
read_board(game, sx, sy)
# Place Ships J2
i=0
for size in ships:
    ## Consume inputs
    s = read_message(game.stdout)
    print s
    s = read_message(game.stdout)
    print s
    ## Place each ships
    s = read_message(j2.stdout)
    mess = s
    print 'Sending message :', mess
    send_message(game.stdin, mess)
    s = read_message(game.stdout)
    print s
    s = read_message(j2.stdout)
    mess = s
    print 'Sending message :', mess
    send_message(game.stdin, mess)

    i = i+1
    read_board(game, sx, sy)
    pause()

#turn = 0
#j1_turns = ['A1','A2','B1','B2','C1','C2','C3','D1','D2','D3','D4','E1','E2','E3','E4','E5']
#j2_turns = ['A1','A2','B1','B2','C1','C2','C3','D1','D2','D3','D4','E1','E2','E3','E4','E5']

while True:
    # Go for battle !!!!
    ## Pass pause :
    s = read_message(game.stdout)
    print s
    send_message(game.stdin, 'o')
    
    ## Read board
    s = read_message(game.stdout)
    print s
    board = read_board(game, sx, sy)
    s = read_message(game.stdout)
    print s
    ## Send player info
    send_message(j1.stdin, str(board))
    ## Get target from AI
    target = read_message(j1.stdout)
    ## Shoot to the game
    send_message(game.stdin, str(target))
    ## Consume human outputs
    s = read_message(game.stdout)
    print s
    read_board(game,sx,sy)
    ## Pass pause
    s = read_message(game.stdout)
    print s

    if s.startswith("Joueur 1 a") and platform.system().lower() == 'windows':
        break
    
    send_message(game.stdin, 'o')
    
    ## Pass pause :
    s = read_message(game.stdout)
    print "DBG", s
    ## If there is no message one player has win the game
    if s == '':
        # Send dummy message to avoid error:
        send_message(j2.stdin, str(board))
        break
    pause()
    send_message(game.stdin, 'o')
    
    ## Read board
    s = read_message(game.stdout)
    print s
    board = read_board(game, sx, sy)
    s = read_message(game.stdout)
    print s
    ## Send player info
    send_message(j2.stdin, str(board))
    ## Get target from AI
    target = read_message(j2.stdout)
    ## Shoot to the game
    send_message(game.stdin, str(target))
    ## Consume human outputs
    s = read_message(game.stdout)
    print s
    read_board(game,sx,sy)
    ## Pass pause
    s = read_message(game.stdout)
    print s

    if s.startswith("Joueur 2 a") and platform.system().lower() == 'windows':
        send_message(j1.stdin, str(board))
        send_message(j2.stdin, str(board))
        break
    ## If there is no message one player has win the game
    if s == '':
        # Send dummy message to avoid error:
        send_message(j1.stdin, str(board))
        break
    pause()
    send_message(game.stdin, 'o')


game.stdin.close()
game.stdout.close()
game.terminate()

j1.stdin.close()
j1.stdout.close()
j1.terminate()

j2.stdin.close()
j2.stdout.close()
j2.terminate()

