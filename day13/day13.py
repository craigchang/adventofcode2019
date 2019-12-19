import intCodeProgram
import matplotlib.pyplot as plt

def execute(intCode):
    ptr = relativeBase = 0
    inputs = []
    while intCode[ptr] != 99:
        output, ptr, relativeBase = intCodeProgram.execute(intCode, inputs, ptr, relativeBase)
        if intCode[ptr] == 99 or intCode[ptr] == 3:
            break
        
    return output

def createGameBoard(output, gameBoardMap=dict()):
    #gameBoardMap = dict()
    for i in range(0, len(output), 3):
        x, y, tileId = output[i], output[i+1], output[i+2]
        gameBoardMap[(x,y)] = tileId
    return gameBoardMap

def calculateNumBlockTiles(output):
    gameBoardMap = createGameBoard(output)
    numEmpty = len([k for k,v in gameBoardMap.items() if gameBoardMap[(k[0],k[1])] == 0]) #empty
    numWall = len([k for k,v in gameBoardMap.items() if gameBoardMap[(k[0],k[1])] == 1]) #wall
    numBlock = len([k for k,v in gameBoardMap.items() if gameBoardMap[(k[0],k[1])] == 2]) #block
    numPaddle = len([k for k,v in gameBoardMap.items() if gameBoardMap[(k[0],k[1])] == 3]) #paddle
    numBall = len([k for k,v in gameBoardMap.items() if gameBoardMap[(k[0],k[1])] == 4]) #ball
    return gameBoardMap, numEmpty, numWall, numBlock, numPaddle, numBall

def showGameBoard(gameBoardMap):
    # wall
    xWall = [i[0] for i in gameBoardMap.keys() if gameBoardMap[i] == 1]
    yWall = [i[1] for i in gameBoardMap.keys() if gameBoardMap[i] == 1]
    # blocks
    xBlock = [i[0] for i in gameBoardMap.keys() if gameBoardMap[i] == 2]
    yBlock = [i[1] for i in gameBoardMap.keys() if gameBoardMap[i] == 2]
    # paddle
    xPaddle = [i[0] for i in gameBoardMap.keys() if gameBoardMap[i] == 3]
    yPaddle = [i[1] for i in gameBoardMap.keys() if gameBoardMap[i] == 3]
    # ball
    xBall = [i[0] for i in gameBoardMap.keys() if gameBoardMap[i] == 4]
    yBall = [i[1] for i in gameBoardMap.keys() if gameBoardMap[i] == 4]


    # need to adjust window to see 
    plt.plot(xWall, yWall, 'ro', xBlock, yBlock, 'bo', xPaddle, yPaddle, 'go', xBall, yBall, 'yo')
    plt.grid(True)
    plt.xticks([i for i in range(43)])
    plt.yticks([i for i in range(25)])
    plt.show()

def execute2(intCode):
    ptr = relativeBase = 0
    inputs = []
    gameBoardMap = dict()
    intCode[0] = 2
    while intCode[ptr] != 99:
        output, ptr, relativeBase = intCodeProgram.execute(intCode, inputs, ptr, relativeBase)
        if intCode[ptr] == 99:
            break
        elif intCode[ptr] == 3:
            gameBoardMap = createGameBoard(output, gameBoardMap)
            xBall = list(gameBoardMap.keys())[list(gameBoardMap.values()).index(4)][0]
            xPaddle = list(gameBoardMap.keys())[list(gameBoardMap.values()).index(3)][0]
            #print('ball:', xBall, 'paddle:', xPaddle, 'Show score:', gameBoardMap[(-1,0)])
            joystickVal = (xBall > xPaddle) - (xBall < xPaddle)
            inputs.append(joystickVal)        
    return output

def main():
    # part 1
    intCode = intCodeProgram.readFile('day13/input.txt')
    output = execute(intCode)
    gameBoardMap, numEmpty, numWall, numBlock, numPaddle, numBall = calculateNumBlockTiles(output)
    print(numEmpty, numWall, numBlock, numPaddle, numBall)
    print(gameBoardMap)
    showGameBoard(gameBoardMap)

    # part 2
    intCode = intCodeProgram.readFile('day13/input.txt')
    output = execute2(intCode)
    gameBoardMap = createGameBoard(output)
    showGameBoard(gameBoardMap)

    


main()

#1008 too high
# 348 too high