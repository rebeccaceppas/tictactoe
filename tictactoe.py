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
    if (grid[0] & grid[1] & grid[2]) != '   ':
        var = False
    elif (grid[3] & grid[4] & grid[5]) != '   ':
        var = False
    elif (grid[6] & grid[7] & grid[8]) != '   ':
        var = False
    elif (grid[0] & grid[4] & grid[5]) != '   ':
        var = False
    elif (grid[2] & grid[4] & grid[6]) != '   ':
        var = False
    elif (grid[0] & grid[3] & grid[6]) != '   ':
        var = False
    elif (grid[1] & grid[4] & grid[8]) != '   ':
        var = False
    elif (grid[2] & grid[5] & grid[8]) != '   ':
        var = False
    elif len(p) == 9:
        var = False
    else:
        var = True

def result(L):
    if len(L) == 9:
        ask = input('It was a tie! Would you like to play again? (Y/N)\n')
        if ask.upper() == 'Y':
            print('You are are the \'X\' and this is your board\n')
            sampleboard()
            clear()
            game()
        else:
            print('See you next time!')
    elif ((grid[0] & grid[1] & grid[2]) | (grid[3] & grid[4] & grid[5]) | (grid[6] & grid[7] & grid[8]) | (grid[0] & grid[4] & grid[5]) | (grid[2] & grid[4] & grid[6]) | (grid[0] & grid[3] & grid[6]) | (grid[1] & grid[4] & grid[8]) | (grid[2] & grid[5] & grid[8])) == ' X ':
        ask = input('You won! Would you like to play again? (Y/N)\n')
        if ask.upper() == 'Y':
            print('You are are the \'X\' and this is your board\n')
            sampleboard()
            clear()
            game()


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
            rand = random.randint(0,8)
            while str(rand+1) in choices:
                rand = random.randint(0,8)
            grid[rand] = ' O '
            board()
            choices.append(str(rand+1))
            choices.append(play)
            stop(cont, choices)
    
    result(choices)


start = input('Do you want to play tictactoe? (Y/N)\n')
if start.upper() == 'Y':
    print('You are are the \'X\' and this is your board\n')
    sampleboard()
    clear()
    game()
else:
    print('See you next time!')






