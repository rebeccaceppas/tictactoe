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

def stop(var, p):
    if (grid[0:3] or grid[3:6] or grid[6:]) == [' X ']*3:
        print('You won!')
        var = False
    elif [grid[0], grid[3], grid[6]] or [grid[1], grid[4], grid[7]] or [grid[2], grid[5], grid[8]] == [' X ']*3:
        print('You won!')
        var = False
    elif [grid[0], grid[4], grid[8]] or [grid[2], grid[4], grid[6]] == [' X ']*3:
        print('You won!')
        var = False
    elif (grid[0:3] or grid[3:6] or grid[6:]) == [' O ']*3:
        print('You lost!')
        var = False
    elif [grid[0], grid[3], grid[6]] or [grid[1], grid[4], grid[7]] or [grid[2], grid[5], grid[8]] == [' X ']*3:
        print('You lost!')
        var = False
    elif [grid[0], grid[4], grid[8]] or [grid[2], grid[4], grid[6]] == [' O ']*3:
        print('You lost')
        var = False
    elif len(p) == 9:
        print('It was a tie!')
        var = False
    else:
        var = True

""" def stop(var, p):
    if (set(grid[0:3]) | set(grid[3:6]) | set(grid[6:])) == {' X '}:
        print('You won!')
        var = False
    elif (set(grid[0], grid[3], grid[6]) | set(grid[1], grid[4], grid[7]) | set(grid[2], grid[5], grid[8])) == {' X '}:
        print('You won!')
        var = False
    elif (set(grid[0], grid[4], grid[8]) | set(grid[2], grid[4], grid[6])) == {' X '}:
        print('You won!')
        var = False
    elif (set(grid[0:3]) | set(grid[3:6]) | set(grid[6:])) == {' O '}:
        print('You lost!')
        var = False
    elif (set(grid[0], grid[3], grid[6]) | set(grid[1], grid[4], grid[7]) | set(grid[2], grid[5], grid[8])) == {' O '}:
        print('You lost!')
        var = False
    elif (set(grid[0], grid[4], grid[8]) | set(grid[2], grid[4], grid[6])) == {' O '}:
        print('You lost')
        var = False
    elif len(p) == 9:
        print('It was a tie!')
        var = False
    else:
        var = True """
#def stop(var, p):
   # if grid[0:3](grid[0] and grid[1] and grid[2]) != '   ':
    #    var = False
    #elif (grid[3] and grid[4] and grid[5]) != '   ':
     #   var = False
    #elif (grid[6] and grid[7] and grid[8]) != '   ':
     #   var = False
    #elif (grid[0] and grid[4] and grid[5]) != '   ':
     #   var = False
"""     elif (grid[2] and grid[4] and grid[6]) != '   ':
        var = False
    elif (grid[0] and grid[3] and grid[6]) != '   ':
        var = False
    elif (grid[1] and grid[4] and grid[8]) != '   ':
        var = False
    elif (grid[2] and grid[5] and grid[8]) != '   ':
        var = False
    elif len(p) == 9:
        var = False
    else:
        var = True
 """
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
            while str(rand+1) in choices:
                rand = random.randint(0,8)
            grid[rand] = ' O '
            board()
            choices.append(str(rand+1))
            #stop(cont, choices)
            if len(choices) == 9:
                cont = False
        
    
    ask = input('Do you want to play again? (Y/N)\n')
    if ask.upper() == 'Y':
        print('You are are the \'X\' and this is your board\n')
        sampleboard()
        clear()
        game()
    else:
        print('See you next time!')


start = input('Do you want to play tictactoe? (Y/N)\n')
if start.upper() == 'Y':
    print('This is your board\n')
    sampleboard()
    clear()
    game()
else:
    print('See you next time!')






