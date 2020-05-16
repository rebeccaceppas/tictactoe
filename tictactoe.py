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
    count = 0
    
    while count == 0:

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
            if (grid[0:3] == [' X ']*3) or (grid[3:6] == [' X ']*3) or (grid[6:] == [' X ']*3):
                print('You won!')
                board()
                count += 10
                break
            elif ([grid[0], grid[3], grid[6]] == [' X ']*3) or ([grid[1], grid[4], grid[7]] == [' X ']*3) or ([grid[2], grid[5], grid[8]] == [' X ']*3):
                print('You won!')
                board()
                count += 10
                break
            elif ([grid[0], grid[4], grid[8]] == [' X ']*3) or ([grid[2], grid[4], grid[6]] == [' X ']*3):
                print('You won!')
                board()
                count += 10
                break
            elif (grid[0:3] == [' O ']*3) or (grid[3:6] == [' O ']*3) or (grid[6:] == [' O ']*3):
                print('You lost!')
                board()
                count += 10
                break
            elif ([grid[0], grid[3], grid[6]] == [' O ']*3) or ([grid[1], grid[4], grid[7]] == [' O ']*3) or ([grid[2], grid[5], grid[8]] == [' O ']*3):
                print('You lost!')
                board()
                count += 10
                break
            elif ([grid[0], grid[4], grid[8]] == [' O ']*3) or ([grid[2], grid[4], grid[6]] == [' O ']*3):
                print('You lost')
                board()
                count += 10
                break
            elif len(choices) == 9:
                print('It was a tie!')
                board()
                count += 10
                break
            else:
                count = 0
            rand = random.randint(0,8)
            while str(rand+1) in choices:
                rand = random.randint(0,8)
            grid[rand] = ' O '
            board()
            choices.append(str(rand+1))
            if (grid[0:3] == [' X ']*3) or (grid[3:6] == [' X ']*3) or (grid[6:] == [' X ']*3):
                print('You won!')
                count += 10
                break
            elif ([grid[0], grid[3], grid[6]] == [' X ']*3) or ([grid[1], grid[4], grid[7]] == [' X ']*3) or ([grid[2], grid[5], grid[8]] == [' X ']*3):
                print('You won!')
                count += 10
                break
            elif ([grid[0], grid[4], grid[8]] == [' X ']*3) or ([grid[2], grid[4], grid[6]] == [' X ']*3):
                print('You won!')
                count += 10
                break
            elif (grid[0:3] == [' O ']*3) or (grid[3:6] == [' O ']*3) or (grid[6:] == [' O ']*3):
                print('You lost!')
                count += 10
                break
            elif ([grid[0], grid[3], grid[6]] == [' O ']*3) or ([grid[1], grid[4], grid[7]] == [' O ']*3) or ([grid[2], grid[5], grid[8]] == [' O ']*3):
                print('You lost!')
                count += 10
                break
            elif ([grid[0], grid[4], grid[8]] == [' O ']*3) or ([grid[2], grid[4], grid[6]] == [' O ']*3):
                print('You lost')
                count += 10
                break
            elif len(choices) == 9:
                print('It was a tie!')
                count += 10
                break
            else:
                count = 0
    
    repeat = input('Do you want to play again? (Y/N)\n')
    if repeat.upper() == 'Y':
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
