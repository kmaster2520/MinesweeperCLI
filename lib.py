import numpy as np

def isBomb(pos, grid_raw):
    return grid_raw[pos] > 0.5

def generateGrid(grid_raw):
    height, width = grid_raw.shape
    grid = np.zeros((height,width), dtype=np.int)
    #
    for r in range(height):
        for c in range(width):
            if (isBomb((r,c), grid_raw)):
                grid[r,c] = 9
            else:
                grid[r,c] = countBombs((r,c), grid_raw)
    #
    return grid

def isPointInGrid(pos, grid_shape):
    height, width = grid_shape
    r, c = pos
    return 0 <= r < height and 0 <= c < width

def getSpacesAround(pos, grid_shape):
    r, c = pos
    spaces = [(r-1,c), (r+1,c), (r,c-1), (r,c+1), (r-1,c-1), (r-1,c+1), (r+1,c-1), (r+1,c+1)]
    return [space for space in spaces if isPointInGrid(space, grid_shape)]

def getSpacesAdjacent(pos, grid_shape):
    r, c = pos
    spaces = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
    return [space for space in spaces if isPointInGrid(space, grid_shape)]

def countBombs(pos, grid_raw):
    spaces = getSpacesAround(pos, grid_raw.shape)
    count = 0
    for space in spaces:
        if (isBomb(space, grid_raw)):
            count += 1
    return count

def printGrid(grid_game, grid):
    height, width = grid.shape
    for r in range(height):
        for c in range(width):
            if (grid_game[r,c] == 0):
                print('-  ', end='')
            else:
                if (grid[r,c] == 9):
                    print('x  ', end='')
                elif (grid[r,c] == 0):
                    print('.  ', end='')
                else:
                    print(str(grid[r,c]) + '  ', end='')
        print()

def printGridPretty(grid_game, grid):
    height, width = grid.shape
    #
    print('+---'*(width+1), end='+\n')
    for c in range(width+1):
        print('| %2d'%c, end='')
    print('|')
    #
    for r in range(height):
        print('+---'*(width+1), end='+\n')
        print('|%2d '%(r+1), end='')
        for c in range(width):
            # '| * '
            print('| ', end='')
            if (grid_game[r,c] == 0):
                print('-', end='')
            else:
                if (grid[r,c] == 9):
                    print('x', end='')
                elif (grid[r,c] == 0):
                    print(' ', end='')
                else:
                    print(str(grid[r,c]), end='')
            print(' ', end='')
        print('|',end='\n')
    print('+---'*(width+1), end='+\n\n')

def floodFillZero(pos, grid_game, grid):
    if (not isPointInGrid(pos, grid.shape)):
        return
    if (grid[pos] > 8):
        return
    #
    grid_game[pos] = 1
    if (grid[pos] == 0):
        spaces = getSpacesAdjacent(pos, grid.shape)
        for space in spaces:
            if (grid_game[space] == 0):
                floodFillZero(space, grid_game, grid)

def foundAllSpaces(grid_game, grid):
    height, width = grid.shape
    for r in range(height):
        for c in range(width):
            if (grid_game[r,c] == 0 and grid[r,c] < 9):
                return False
    return True