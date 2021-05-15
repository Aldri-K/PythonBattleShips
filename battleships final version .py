import random

from random import randint
#empty list
board = []
#adds 7 rows to list board[]
for x in range(8):
    #puts O in board
    board.append(["O"] * 8)

#creates function
def printb(board):
    for x in board:
        print(" ".join(x))

#prints the board using the new function
printb(board)


#player ship
print("Captain, where would you like to put the ship?:")
x_axis_s = int(input("X axis 0-7 : "))
y_axis_s = int(input("Y axis 0-7 : "))

board[x_axis_s][y_axis_s] = "X"
printb(board)


#npc ship 1
x_npc_s1 = random.randint(1,7)
print("1x = ",x_npc_s1)
y_npc_s1 = random.randint(1,7)
print("1y = ",y_npc_s1)
board[x_npc_s1][y_npc_s1] = "V"

#npc ship 2
x_npc_s2 = random.randint(1,7)
print("2x = ",x_npc_s2)
y_npc_s2 = random.randint(1,7)
print("2y = ",y_npc_s2)
board[x_npc_s2][y_npc_s2] = "V"

#npc ship 3
x_npc_s3 = random.randint(1,7)
print("3x = ",x_npc_s3)
y_npc_s3 = random.randint(1,7)
print("3y = ",y_npc_s3)
board[x_npc_s3][y_npc_s3] = "V"

#npc ship 4
x_npc_s4 = random.randint(1,7)
print("4x = ",x_npc_s4)
y_npc_s4 = random.randint(1,7)
print("4y = ",y_npc_s4)
board[x_npc_s4][y_npc_s4] = "V"

print("Captain I see something in the distance...")

#creates a delay
import time
time.sleep(1.5)

print("Its a ship Captain!\nThey are aiming their artillery at us\nWe can't see anything until this fog lifts!")
print("We are going to have to guess their coordinates captain!")



#repeats code until hit = 1
hit = 0
en_ship1 = 0
en_ship2 = 0
en_ship3 = 0
en_ship4 = 0
rem_ship = 4
damage = 0
while hit != 4 and damage < 3:

    #updates the board everytime
    printb(board)
    print("I see ",rem_ship,"ships")
    print("Fire at the enemy!")
    x_shot = int(input("An X coordinate Captain : "))
    y_shot = int(input("A Y coordinate Captain : "))

    #checks is shot coords are the same as enemy ship
    if x_shot == x_npc_s1 and y_shot == y_npc_s1 and en_ship1 != 1:
        print("Good shot Captain! They're going down\n")
        hit = hit +1
        rem_ship = rem_ship -1
        board[x_npc_s1][y_npc_s1] = "O"
        en_ship1 = en_ship1 +1

    elif x_shot == x_npc_s2 and y_shot == y_npc_s2:
        print("Good shot Captain! They're going down\n")
        hit = hit +1
        rem_ship = rem_ship -1
        board[x_npc_s2][y_npc_s2] = "O"
        en_ship2 = en_ship2 +1

    elif x_shot == x_npc_s3 and y_shot == y_npc_s3:
        print("Good shot Captain! They're going down\n")
        hit = hit +1
        rem_ship = rem_ship -1
        board[x_npc_s3][y_npc_s3] = "O"
        en_ship3 = en_ship3 +1

    elif x_shot == x_npc_s4 and y_shot == y_npc_s4:
        print("Good shot Captain! They're going down\n")
        hit = hit +1
        rem_ship = rem_ship -1
        board[x_npc_s4][y_npc_s4] = "O"
        en_ship4 = en_ship4 +1
        
    else:
        print("You missed Captain!\n")

    time.sleep(0.5) 
    #npc shot coords are randomly generated
    npc_shotx = random.randint(1,7)
    npc_shoty = random.randint(1,7)

    if en_ship1 != 1:
        if npc_shotx == x_axis_s and npc_shoty == y_axis_s:
            print("They hit us Captain")
            damage = damage +1
        else:
            print("They fire and missed Captain\n")

    npc_shotx2 = random.randint(1,7)
    npc_shoty2 = random.randint(1,7)

    if en_ship2 != 1:
        if npc_shotx2 == x_axis_s and npc_shoty2 == y_axis_s and en_ship2 != 1:
            print("They hit us Captain")
            damage = damage +1
        else:
            print("They fire and missed Captain\n")

    npc_shotx3 = random.randint(1,7)
    npc_shoty3 = random.randint(1,7)

    if en_ship3 != 1:
        if npc_shotx3 == x_axis_s and npc_shoty3 == y_axis_s and en_ship3 != 1:
            print("They hit us Captain")
            damage = damage +1
        else:
            print("They fire and missed Captain\n")

    npc_shotx4 = random.randint(1,7)
    npc_shoty4 = random.randint(1,7)

    if en_ship4 != 1:
        if npc_shotx4 == x_axis_s and npc_shoty3 == y_axis_s and en_ship4 != 1:
            print("They hit us Captain")
            damage = damage +1
        else:
            print("They fire and missed Captain\n")

    
if damage == 2:
    
    time.sleep(0.5)
    print("We are going down Captain!")

if rem_ship == 0:
    print("We won the batlle!")




    

    

