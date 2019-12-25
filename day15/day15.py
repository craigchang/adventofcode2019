import intCodeProgram
import matplotlib.pyplot as plt

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4
DIRECTIONS = [NORTH, SOUTH, WEST, EAST]

WALL = 0
MOVED = 1
MOVED_AND_GOAL = 2

def solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x=0, y=0, ptr=0, relativeBase=0):
    outputVal, ptr, relativeBase = intCodeProgram.execute(intCode, [DIRECTIONS[directionIndex]], ptr, relativeBase)
    outputVal = outputVal[0]
    printMaze(mazeDict)
    
    if outputVal == MOVED_AND_GOAL: # if found
        print('found at %d,%d' % (x, y))
        return True
    elif (x,y) in wasHereDict and wasHereDict[(x,y)] == '#': # if wall
        print('wall at %d,%d' % (x, y))
        return False
    elif (x,y) in wasHereDict and wasHereDict[(x,y)] == '.': # if visited
        print('visited at %d,%d' % (x, y))
        return False

    direction = DIRECTIONS[directionIndex] # get current direction

    if outputVal == WALL:
        if direction == NORTH:
            mazeDict[(x,y+1)] = '#'
        elif direction == SOUTH:
            mazeDict[(x,y-1)] = '#'
        elif direction == WEST:
            mazeDict[(x-1,y)] = '#'
        elif direction == EAST:
            mazeDict[(x+1,y)] = '#'
        
        directionIndex = directionIndex + 1 if directionIndex < 3 else 0 # change directions
        solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase)

    if outputVal == MOVED:
        mazeDict[(x,y)] = '.'
        wasHereDict[(x,y)] = '.' # marked current position as visited
        if direction == NORTH:
            y += 1
        elif direction == SOUTH:
            y -= 1
        elif direction == WEST:
            x -= 1
        elif direction == EAST:
            x += 1
        mazeDict[(x,y)] = 'D'


    if solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase):
        correctPathDict[(x,y)] = '.'
        return True

    directionIndex = directionIndex + 1 if directionIndex < 3 else 0 # change directions
    if solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase):
        correctPathDict[(x,y)] = '.'
        return True

    directionIndex = directionIndex + 1 if directionIndex < 3 else 0 # change directions
    if solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase):
        correctPathDict[(x,y)] = '.'
        return True
    
    directionIndex = directionIndex + 1 if directionIndex < 3 else 0 # change directions
    if solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase):
        correctPathDict[(x,y)] = '.'
        return True

        # if solve(intCode, mazeDict, wasHereDict, correctPathDict, directionIndex, x, y, ptr, relativeBase):
        #     correctPathDict[(x,y)] = '.'
        #     return True
            #directionIndex = directionIndex + 1 if directionIndex < 3 else 0
    return False
                    

def printMaze(mazeDict):
    # walls
    xWall = [i[0] for i in mazeDict.keys() if mazeDict[i] == '#']
    yWall = [i[1] for i in mazeDict.keys() if mazeDict[i] == '#']
    # path
    xPath = [i[0] for i in mazeDict.keys() if mazeDict[i] == '.']
    yPath = [i[1] for i in mazeDict.keys() if mazeDict[i] == '.']
    # drone
    xDrone = [i[0] for i in mazeDict.keys() if mazeDict[i] == 'D']
    yDrone = [i[1] for i in mazeDict.keys() if mazeDict[i] == 'D']


    plt.plot(xWall, yWall, 'ro', xPath, yPath, 'bo', xDrone, yDrone, 'yo')
    plt.grid(True)
    #plt.xticks([i for i in range(43)])
    #plt.yticks([i for i in range(25)])
    plt.show()

def main():
    intCode = intCodeProgram.readFile("day15/input.txt")

    # north = 1
    # south = 2
    # west = 3
    # east = 4

    mazeDict = dict()
    wasHereDict = dict()
    correctPathDict = dict()
    mazeDict[(0,0)] = 'D'
    wasHereDict[(0,0)] = 'D'

    solve(intCode, mazeDict, wasHereDict, correctPathDict, 0)

    printMaze(mazeDict)

    

main()