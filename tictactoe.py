import random

grid = ['   ']*9

def board():
    
    print(grid[0]+'|'+grid[1]+'|'+grid[2])
    print('---|---|---')
    print(grid[3]+'|'+grid[4]+'|'+grid[5])
    print('---|---|---')
    print(grid[6]+'|'+grid[7]+'|'+grid[8])

def sampleboard():
    board = '\n  1 | 2 | 3 \n ---|---|--- \n  4 | 5 | 6 \n ---|---|--- \n  7 | 8 | 9 \n ---|---|--- \n'
    print(board)


def replace(x):
    empty = '\n    |   |   \n ---|---|--- \n    |   |   \n ---|---|--- \n    |   |   \n ---|---|--- \n'
    if x == 1:
        empty = '\n  X |   |   \n ---|---|--- \n    |   |   \n ---|---|--- \n    |   |   \n ---|---|--- \n'
    

def game():
    
    choices = []
    play = input('Where do you want to put your first X? (1-9)')


    

    pass




start = input('Do you want to play tictactoe? (Y/N)\n')
if start.upper() == 'Y':
    print('You are are the \'X\' and this is your board')
    board()
    game()


else:
    print('See you next time!')






