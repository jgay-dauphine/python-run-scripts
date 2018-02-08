from random import randint


turns = ['A1','A2','B1','B2','C1','C2','C3','D1','D2','D3','D4','E1','E2','E3','E4','E5']

# Grid DATA :
# 0 : 
# 1 : 
# 2 : 
# 3 : 

# Read grid size
size_x = int(input())
size_y = int(input())

# Read ships
ships = input()

# Place ships
print "A1"
print "v"
print "B1"
print "v"
print "C1"
print "v"
print "D1"
print "v"
print "E1"
print "v"


# Go to war !
turn = 0
while True:
    # Read grid
    grid = input()
    # select attack
    target = turns[turn]
    # fire weapons
    print target
    turn = turn + 1

