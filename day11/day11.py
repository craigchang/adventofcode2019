import intCodeProgram
import matplotlib.pyplot as plt

DIRECTIONS = ('up', 'right', 'down', 'left')

def getDirection(d, dIndex):
    if d == 1:
        dIndex += 1
        if dIndex >= 4:
            dIndex = 0
    else:
        dIndex -= 1
        if dIndex < 0:
            dIndex = 3
    return DIRECTIONS[dIndex], dIndex

def getFloorValue(floorColor):
    return 0 if floorColor == '.' else 1

def getFloorColor(floorValue):
    return '.' if floorValue == 0 else '#'

def moveRobot(d, dIndex, xR, yR):
    direction, dIndex = getDirection(d, dIndex)
    if direction == 'up':
        yR += 1
    elif direction == 'right':
        xR += 1
    elif direction == 'left':
        xR -= 1
    else:
        yR -= 1
    return xR, yR, dIndex

def drawMessage(robotMap):
    xAxis = [i[0] for i in robotMap.keys() if robotMap[i] == '#']
    yAxis = [i[1] for i in robotMap.keys() if robotMap[i] == '#']

    # need to adjust window to see 
    plt.plot(xAxis, yAxis, 'ro')
    plt.show()

def execute(intCode, inputs):
    robotMap = dict()
    robotMap[(0,0)] = getFloorColor(inputs[0])
    initVal = inputs[0] 
    xR, yR = (0,0)
    ptr = relativeBase = dIndex = 0

    while intCode[ptr] != 99:
        output, ptr, relativeBase = intCodeProgram.execute(intCode, inputs, ptr, relativeBase)
        if intCode[ptr] == 99:
            break
        robotMap[(xR,yR)] = getFloorColor(output[0])
        xR, yR, dIndex = moveRobot(output[1], dIndex, xR, yR)
        if (xR,yR) not in robotMap:
            inputs.append( initVal )
        else:
            inputs.append( getFloorValue(robotMap[(xR,yR)]) )
    return robotMap

def main():
    intCode = intCodeProgram.readFile('day11/input.txt')
    robotMap = execute(intCode, [0])
    print(len(robotMap))

    intCode = intCodeProgram.readFile('day11/input.txt')
    robotMap = execute(intCode, [1])
    drawMessage(robotMap) # need to adjust window to see message better
    
main()
