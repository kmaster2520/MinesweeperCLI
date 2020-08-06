import numpy as np
from lib import *

width = 15
height = 10
density = 0.2

grid_raw = np.random.binomial(1, density, width * height).reshape(height, width)
grid = generateGrid(grid_raw)        
#print(grid_raw)
#print(grid)


grid_game = np.zeros((height,width), dtype=np.int)
# GAME LOOP

# steps: choose position, flip over (use floodfill zero)
row = 0
col = 0
pos = (0,0)
command = ''
args = []

firstMove = True # make sure first move isn't a bomb space

gameOver = False
while not gameOver:
    while 1:
        action = input('> ').split(' ')
        if (len(action) == 0):
            continue
        command = action[0]
        args = action[1:]
        #
        if (command == 'move' or command == 'm'):
            command = 'move'
            if (len(args) != 2):
                print('Error: must have two integers as coordinates')
                continue
            try:
                row = int(args[0])
                col = int(args[1])
                if (not isPointInGrid((row,col), grid.shape)):
                    print('Error: point out of bounds')
                    continue
                break
            except:
                print('Error: must have two integers as coordinates')
                continue
    #
    pos = (row, col)
    #
    if (command == 'move'):
        if (firstMove):
            countBombs = 0
            spaces = getSpacesAround(pos, grid.shape)
            for space in spaces:
                if (1 <= grid[space] <= 8):
                    grid[space] -= 1
                if (isBomb(space, grid_raw)):
                    countBombs += 1
            grid[pos] = countBombs
            firstMove = False

        if (grid[row,col] > 8):
            grid_game[pos] = 1
            gameOver = True
            print('You found a bomb. You lose.')
        else:
            floodFillZero(pos, grid_game, grid)
    #
    printGridPretty(grid_game, grid)
    #
    if (foundAllSpaces(grid_game, grid)):
        gameOver = True
        print('You win.')

'''
+ - + - +
| x | 1 |
+ - + - +
'''
    

