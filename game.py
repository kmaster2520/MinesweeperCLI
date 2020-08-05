import numpy as np
from lib import *

width = 10
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

gameOver = False
while not gameOver:
    while 1:
        row = int(input('Choose row:  '))
        col = int(input('Choose column:  '))
        if (isPointInGrid((row,col), grid.shape)):
            break
        else:
            print('Error, pick a valid point')
    #
    if (grid[row,col] > 8):
        grid_game[row,col] = 1
        gameOver = True
        print('You found a bomb. You lose.')
    else:
        floodFillZero((row, col), grid_game, grid)
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
    

