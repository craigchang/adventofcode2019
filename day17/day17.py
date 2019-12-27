import intCodeProgram
import matplotlib.pyplot as plt

DRONE_DIRECTIONS = ["^", "<", "v", ">"] 

def turnRight(droneDirection, pathMap):
    i = DRONE_DIRECTIONS.index(droneDirection) - 1
    pathMap.append("R")
    pathMap.append(",")
    return 3 if i < 0 else i

def turnLeft(droneDirection, pathMap):
    i = DRONE_DIRECTIONS.index(droneDirection) + 1
    pathMap.append("L")
    pathMap.append(",")
    return 0 if i > 3 else i

def moveLeft(scaffoldDict, x, y, pathMap):
    steps = 0
    while x-1 >= 0 and scaffoldDict[(x-1,y)] == '#':
        x -= 1
        steps += 1
    pathMap.append(str(steps))
    pathMap.append(",")
    return x, steps

def moveRight(scaffoldDict, x, y, xSize, pathMap):
    steps = 0
    while x+1 <= xSize and scaffoldDict[(x+1,y)] == '#':
        x += 1
        steps += 1
    pathMap.append(str(steps))
    pathMap.append(",")
    return x, steps

def moveUp(scaffoldDict, x, y, pathMap):
    steps = 0
    while y+1 <= 0 and scaffoldDict[(x,y+1)] == '#':
        y += 1
        steps += 1
    pathMap.append(str(steps))
    pathMap.append(",")
    return y, steps

def moveDown(scaffoldDict, x, y, ySize, pathMap):
    steps = 0
    while y-1 >= ySize and scaffoldDict[(x,y-1)] == '#':
        y -= 1
        steps += 1
    pathMap.append(str(steps))
    pathMap.append(",")
    return y, steps

def isDrone(d):
    return d in DRONE_DIRECTIONS

def showMap(scaffoldDict):
    # scaffold
    xScaffold = [i[0] for i in scaffoldDict.keys() if scaffoldDict[i] == '#']
    yScaffold = [i[1] for i in scaffoldDict.keys() if scaffoldDict[i] == '#']
    # space
    xSpace = [i[0] for i in scaffoldDict.keys() if scaffoldDict[i] == '.']
    ySpace = [i[1] for i in scaffoldDict.keys() if scaffoldDict[i] == '.']
    # drone
    xDrone = [i[0] for i in scaffoldDict.keys() if isDrone(scaffoldDict[i])]
    yDrone= [i[1] for i in scaffoldDict.keys() if isDrone(scaffoldDict[i])]
    #sizes
    xSize = max(scaffoldDict.keys())[0]
    ySize = min(scaffoldDict.keys())[1]

    plt.plot(xScaffold, yScaffold, 'ro', xSpace, ySpace, 'bo', xDrone, yDrone, 'yo')
    plt.grid(True)
    plt.xticks([i for i in range(xSize)])
    plt.yticks([i for i in range(0, ySize, -1)])
    plt.show()

def createMap(intCode):
    output, ptr, relativeBase = intCodeProgram.execute(intCode, [0])
    scaffoldDict = dict()

    x = y = 0
    for i in output:
        if i == 35:
            scaffoldDict[(x,y)] = '#'
            x += 1
        elif i == 46:
            scaffoldDict[(x,y)] = '.'
            x += 1
        elif i == 74:
            scaffoldDict[(x,y)] = '<'
            x += 1
        elif i == 76:
            scaffoldDict[(x,y)] = '<'
            x += 1
        elif i == 94:
            scaffoldDict[(x,y)] = '^'
            x += 1
        elif i == 166:
            scaffoldDict[(x,y)] = 'v'
            x += 1
        elif i == 10: # newlines
            x = 0
            y -= 1
    return scaffoldDict

def part1(scaffoldDict):
    xSize = max(scaffoldDict.keys())[0]
    ySize = min(scaffoldDict.keys())[1]

    sumParms = 0
    for k,v in scaffoldDict.items():
        x,y = k
        if (x-1) >= 0 and (y-1) >= ySize and (x+1) <= xSize and (y+1) <= 0:
            if (scaffoldDict[(x,y)] == '#' and 
                scaffoldDict[(x+1,y)] == '#' and 
                scaffoldDict[(x-1,y)] == '#' and 
                scaffoldDict[(x,y+1)] == '#' and 
                scaffoldDict[(x,y-1)] == '#'):
                sumParms += (x * abs(y))
    print(sumParms)

def part2(scaffoldDict, intCode):
    xSize = max(scaffoldDict.keys())[0]
    ySize = min(scaffoldDict.keys())[1]

    droneX, droneY = [i for i in scaffoldDict.keys() if isDrone(scaffoldDict[i])][0]
    droneDirection = scaffoldDict[(droneX, droneY)]
    droneIndex = DRONE_DIRECTIONS.index(droneDirection)

    pathMap = []

    while True:
        if droneDirection == "^":
            if droneX-1 >= 0 and scaffoldDict[(droneX-1, droneY)] == '#':
                droneIndex = turnLeft(droneDirection, pathMap)
                droneX, steps = moveLeft(scaffoldDict, droneX, droneY, pathMap)
            elif droneX+1 <= xSize and scaffoldDict[(droneX+1, droneY)] == '#':
                droneIndex = turnRight(droneDirection, pathMap)
                droneX, steps = moveRight(scaffoldDict,droneX,droneY,xSize,pathMap)
            else:
                break

        elif droneDirection == "v":
            if droneX-1 >= 0 and scaffoldDict[(droneX-1, droneY)] == '#':
                droneIndex = turnRight(droneDirection, pathMap)
                droneX, steps = moveRight(scaffoldDict,droneX,droneY,xSize,pathMap)
            elif droneX+1 <= xSize and scaffoldDict[(droneX+1, droneY)] == '#':
                droneIndex = turnLeft(droneDirection, pathMap)
                droneX, steps = moveLeft(scaffoldDict, droneX, droneY, pathMap)
            else:
                break

        elif droneDirection == "<":
            if droneY+1 <= 0 and scaffoldDict[(droneX, droneY+1)] == '#':
                droneIndex = turnRight(droneDirection, pathMap)
                droneY, steps = moveUp(scaffoldDict,droneX,droneY,pathMap)
            elif droneY-1 >= ySize and scaffoldDict[(droneX, droneY-1)] == '#':
                droneIndex = turnLeft(droneDirection, pathMap)
                droneY, steps = moveDown(scaffoldDict,droneX,droneY,ySize,pathMap)
            else:
                break

        elif droneDirection == ">":
            if droneY+1 <= 0 and scaffoldDict[(droneX, droneY+1)] == '#':
                droneIndex = turnLeft(droneDirection, pathMap)
                droneY, steps = moveUp(scaffoldDict,droneX,droneY,pathMap)
            elif droneY-1 >= ySize and scaffoldDict[(droneX, droneY-1)] == '#':
                droneIndex = turnRight(droneDirection, pathMap)
                droneY, steps = moveDown(scaffoldDict,droneX,droneY,ySize,pathMap)
            else:
                break

        scaffoldDict[(droneX,droneY)] = DRONE_DIRECTIONS[droneIndex]
        droneDirection = DRONE_DIRECTIONS[droneIndex]

    return executeProgram(pathMap, intCode)

def executeProgram(pathMap, intCode):
    main = list(map(ord, ['A', ',', 'B', ',', 'B', ',', 'C', ',', 'B', ',', 'C', ',', 'B', ',', 'C', ',', 'A', ',', 'A']))
    main.append(10)
    A = list(map(ord, ['L', ',', '6', ',', 'R', ',', '8', ',', 'L', ',', '4', ',', 'R', ',', '8', ',', 'L', ',', '1', '2']))
    A.append(10)
    B = list(map(ord, ['L', ',', '1', '2', ',', 'R', ',', '1', '0', ',', 'L', ',', '4']))
    B.append(10)
    C = list(map(ord, ['L', ',', '1', '2', ',', 'L', ',', '6', ',', 'L', ',', '4', ',', 'L', ',', '4']))
    C.append(10)
    continuousFeed = list(map(ord, ['n']))
    continuousFeed.append(10)

    intCode[0] = 2 # start the robot

    print('starting the drone')
    output, ptr, relativeBase = intCodeProgram.execute(intCode, [])

    print('entering main routine:', main)
    output, ptr, relativeBase = intCodeProgram.execute(intCode, main, ptr, relativeBase)

    print('entering function A:', A)
    output, ptr, relativeBase = intCodeProgram.execute(intCode, A, ptr, relativeBase)

    print('entering function B:', B)
    output, ptr, relativeBase = intCodeProgram.execute(intCode, B, ptr, relativeBase)

    print('entering function C:', C)
    output, ptr, relativeBase = intCodeProgram.execute(intCode, C, ptr, relativeBase)

    print('entering continuous feed:', continuousFeed)
    output, ptr, relativeBase = intCodeProgram.execute(intCode, continuousFeed, ptr, relativeBase)

    print('final value:', output[len(output)-1])

    return output[len(output)-1]

def main():
    intCode = intCodeProgram.readFile('day17/input.txt')
    scaffoldDict = createMap(intCode)
    print(part1(scaffoldDict))

    intCode = intCodeProgram.readFile('day17/input.txt')
    print(part2(scaffoldDict, intCode))

main()