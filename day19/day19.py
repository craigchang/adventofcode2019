import intCodeProgram
import matplotlib.pyplot as plt
import copy
import math

def showMap(gridDict, target):
    # scaffold
    xBeam = [i[0] for i in gridDict.keys() if gridDict[i] == 1]
    yBeam = [i[1] for i in gridDict.keys() if gridDict[i] == 1]
    yBeam = list(map(lambda x: -x, yBeam))
    # space
    xSpace = [i[0] for i in gridDict.keys() if gridDict[i] == 0]
    ySpace = [i[1] for i in gridDict.keys() if gridDict[i] == 0]
    ySpace = list(map(lambda x: -x, ySpace))

    plt.plot(xBeam, yBeam, 'ro', xSpace, ySpace, 'bo', [target[0]], [-target[1]], 'yo')
    plt.grid(True)
    plt.show()

def isFit(gridDict,x,y,scale):
    return (gridDict[(x,y)] == 1 and 
        (x,y-scale) in gridDict and gridDict[(x,y-scale)] == 1 and
        (x-scale,y) in gridDict and gridDict[(x-scale,y)] == 1)

def part1(intCode):
    grid = []

    for y in range(50):
        grid.append([])
        for x in range(50):
            output, ptr, relativeBase = intCodeProgram.execute(copy.deepcopy(intCode),[x,y])
            grid[y].append(output[0])

    numPoints = len([(x,y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 1])
    return numPoints

def part2(intCode):
    gridDict = dict()
    grid = []
    grid.append([])
    targetPoint = (0,0)    
    
    for y in range(0, 10000):
        for x in range(0, 10000):
            if y == 1 or y == 2 or y == 4: # helps skip points that are not needed
                continue
            if y > (2 * x) and y >= 5: # helps skip points that are not needed
                grid[y].append(0)
                continue
            output, ptr, relativeBase = intCodeProgram.execute(copy.deepcopy(intCode),[x,y])
            gridDict[(x,y)] = output[0]
            grid[y].append(output[0])
            if grid[y][x] == 0 and grid[y][x-1] == 1:
                break # if previous point was a beam, then skip the rest of points on x-axis

            if isFit(gridDict,x,y,99):
                targetPoint = (x-99, y-99)
                print('point found: ', targetPoint)
                return targetPoint

        grid.append([])   
    #showMap(gridDict, targetPoint)
    return targetPoint

def main():
    intCode = intCodeProgram.readFile('day19/input.txt')
    print(part1(intCode))

    # slow but works
    intCode = intCodeProgram.readFile('day19/input.txt')
    x,y = part2(intCode)
    print(x * 10000 + y)
main()
