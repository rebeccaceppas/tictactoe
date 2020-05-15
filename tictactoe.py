import random

grid = ['   ']*9

def board():
    
    print(grid[0]+'|'+grid[1]+'|'+grid[2])
    print('---|---|---')
    print(grid[3]+'|'+grid[4]+'|'+grid[5])
    print('---|---|---')
    print(grid[6]+'|'+grid[7]+'|'+grid[8])

def sampleboard():
    for i in range(9):
        grid[i] = ' ' + str(i+1) + ' '
    board()

def clear():
    for i in range(9):
        grid[i] = '   '
    return grid

def replace(x):
    grid[x-1] = ' X '

def game(): 
    choices = []
    rand = 0
    cont = True
    while cont:

        play = input('Where do you want to put your X? (1-9)\n')
        if play not in ['1','2','3','4','5','6','7','8','9']:
            print('Invalid input, try again\n')
            board()
        elif play in choices:
            print('This box is taken, choose again.\n')
            board()
        else:
            replace(int(play))
            choices.append(play)
            rand = random.randint(0,8)
            while (rand+1) in choices:
                rand = random.randint(0,8)
            grid[rand] = ' O '
            board()
            choices.append(rand+1)

            


        #what it input is not 1-9
        #set cont = function() that checks if row, column or diagonal has all Xs or Os or if all squares have been filled
    


start = input('Do you want to play tictactoe? (Y/N)\n')
if start.upper() == 'Y':
    print('You are are the \'X\' and this is your board\n')
    sampleboard()
    clear()
    game()
else:
    print('See you next time!')






