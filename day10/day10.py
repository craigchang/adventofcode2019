from itertools import permutations
import math

def readFile(fileName):
    file = open(fileName, "r")
    grid = []
    for line in file.readlines():
        grid.append([p for p in line.rstrip()])
    return grid

def getAllSlopesForAsteriod(xSize, ySize):
    allSlopes = set()

    for i in range(-xSize + 1, xSize, 1):
        for j in range(-ySize + 1, ySize, 1):
            if j == 0: # y-axis
                allSlopes.add((1,0))
                allSlopes.add((-1,0))
            elif i == 0: # x-axis
                allSlopes.add((0,1))
                allSlopes.add((0,-1))
            else: # get slope of common denominator
                commonD = math.gcd(i,j)
                allSlopes.add( (int(i/commonD), int(j/commonD)) )

    slopesInOrder = []

    # top right slopes
    slopesDict = dict()
    for slope in [slope for slope in allSlopes if slope[0] < 0 and slope[1] > 0]:
        slopesDict[slope] = abs(slope[0])/abs(slope[1])
    slopesInOrder.append((-1,0))
    for key, value in sorted(slopesDict.items(), key=lambda item: item[1], reverse=True):
        slopesInOrder.append(key)

    # bottom right slopes
    slopesDict = dict()
    for slope in [slope for slope in allSlopes if slope[0] > 0 and slope[1] > 0]:
        slopesDict[slope] = abs(slope[0])/abs(slope[1])
    slopesInOrder.append((0,1))
    for key, value in sorted(slopesDict.items(), key=lambda item: item[1]):
        slopesInOrder.append(key)

    # bottm left slopes
    slopesDict = dict()
    for slope in [slope for slope in allSlopes if slope[0] > 0 and slope[1] < 0]:
        slopesDict[slope] = abs(slope[0])/abs(slope[1])
    slopesInOrder.append((1,0))
    for key, value in sorted(slopesDict.items(), key=lambda item: item[1], reverse=True):
        slopesInOrder.append(key)

    # top left slopes
    slopesDict = dict()
    for slope in [slope for slope in allSlopes if slope[0] < 0 and slope[1] < 0]:
        slopesDict[slope] = abs(slope[0])/abs(slope[1])
    slopesInOrder.append((0,-1))
    for key, value in sorted(slopesDict.items(), key=lambda item: item[1]):
        slopesInOrder.append(key)

    return slopesInOrder

def part1(grid):
    xSize = len(grid[0])
    ySize = len(grid)
    x = y = 0

    asteroidList = [(y,x) for y in range(ySize) for x in range(xSize) if grid[x][y] == "#"]
    asteroidMap = dict()
    
    allSlopes = getAllSlopesForAsteriod(xSize, ySize)

    for a in asteroidList:
        visibleAsteroids = 0
        aX,aY = a

        for slope in allSlopes:
            y,x = slope
            if y > 0 and x > 0: # bottom right
                if (aY + y >= ySize) or (aX + x >= xSize): # outside boundaries
                    continue
                for i,j in zip(range(aY+y, ySize, y), range(aX+x, xSize, x)):
                    if grid[i][j] == '#':
                        visibleAsteroids += 1
                        break
            elif y > 0 and x < 0: # bottom left
                if (aY + y >= ySize) or (aX + x < 0): # outside boundaries
                    continue
                for i,j in zip(range(aY+y, ySize, y), range(aX+x, -1, x)):
                    if grid[i][j] == '#':
                        visibleAsteroids += 1
                        break
            elif y < 0 and x > 0: #top right
                if (aY + y < 0) or (aX + x >= xSize): # outside boundaries
                    continue
                for i,j in zip(range(aY+y, -1, y), range(aX+x, xSize, x)):
                    if grid[i][j] == '#':
                        visibleAsteroids += 1
                        break
            elif y < 0 and x < 0: # top left
                if (aY + y < 0) or (aX + x < 0): # outside boundaries
                    continue
                for i,j in zip(range(aY+y, -1, y), range(aX+x, -1, x)):
                    if grid[i][j] == '#':
                        visibleAsteroids += 1
                        break
            elif y > 0 and x == 0: # down
                if (aY + y >= ySize):
                    continue
                for i in range(aY+y, ySize, y):
                    if grid[i][aX] == '#':
                        visibleAsteroids += 1
                        break
            elif y < 0 and x == 0: # up
                if (aY + y < 0):
                    continue
                for i in range(aY+y, -1, y):
                    if grid[i][aX] == '#':
                        visibleAsteroids += 1
                        break
            elif x > 0 and y == 0: # right
                if (aX + x >= xSize):
                    continue
                for i in range(aX+x, xSize, x):
                    if grid[aY][i] == '#':
                        visibleAsteroids += 1
                        break
            elif x < 0 and y == 0: # left
                if (aX + x < 0):
                    continue
                for i in range(aX+x, -1, x):
                    if grid[aY][i] == '#':
                        visibleAsteroids += 1
                        break

        asteroidMap[a] = visibleAsteroids         

    numDetected = 0
    asteroidLocation = 0
    for k,v in asteroidMap.items():
        if numDetected < v:
            numDetected = v
            asteroidLocation = k

    return numDetected, asteroidLocation

def isGridNotEmpty(asteroid, grid, xSize, ySize):
    aX, aY = asteroid
    for i in range(ySize):
        for j in range(xSize):
            if grid[i][j] == '#':
                if i == aY and j == aX:
                    continue
                return True
    return False

def part2(asteroid, grid):
    xSize = len(grid[0])
    ySize = len(grid)
    x = y = 0
    aX,aY = asteroid

    asteroidsDestroyedMap = dict()
    numAsteroidDestroyed = 0

    slopesList = getAllSlopesForAsteriod(xSize, ySize)

    while(isGridNotEmpty(asteroid, grid, xSize, ySize)):
        for slope in slopesList:
            y,x = slope
            if y > 0 and x > 0: # bottom right
                if (aY + y >= ySize) or (aX + x >= xSize): # outside boundaries
                    continue
                for i,j in zip(range(aY+y, ySize, y), range(aX+x, xSize, x)):
                    if grid[i][j] == '#':
                        grid[i][j] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (j, i)
                        numAsteroidDestroyed += 1
                        break
            elif y > 0 and x < 0: # bottom left
                if (aY + y >= ySize) or (aX + x < 0):
                    continue
                for i,j in zip(range(aY+y, ySize, y), range(aX+x, -1, x)):
                    if grid[i][j] == '#':
                        grid[i][j] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (j, i)
                        numAsteroidDestroyed += 1
                        break
            elif y < 0 and x > 0: #top right
                if (aY + y < 0) or (aX + x >= xSize):
                    continue
                for i,j in zip(range(aY+y, -1, y), range(aX+x, xSize, x)):
                    if grid[i][j] == '#':
                        grid[i][j] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (j, i)
                        numAsteroidDestroyed += 1
                        break
            elif y < 0 and x < 0: # top left
                if (aY + y < 0) or (aX + x < 0):
                    continue
                for i,j in zip(range(aY+y, -1, y), range(aX+x, -1, x)):
                    if grid[i][j] == '#':
                        grid[i][j] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (j, i)
                        numAsteroidDestroyed += 1
                        break
            elif y > 0 and x == 0: # down
                if (aY + y >= ySize):
                    continue
                for i in range(aY+y, ySize, y):
                    if grid[i][aX] == '#':
                        grid[i][aX] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (aX, i)
                        numAsteroidDestroyed += 1
                        break
            elif y < 0 and x == 0: # up
                if (aY + y < 0):
                    continue
                for i in range(aY+y, -1, y):
                    if grid[i][aX] == '#':
                        grid[i][aX] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (aX, i)
                        numAsteroidDestroyed += 1
                        break
            elif x > 0 and y == 0: # right
                if (aX + x >= xSize):
                    continue
                for i in range(aX+x, xSize, x):
                    if grid[aY][i] == '#':
                        grid[aY][i] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (i, aY)
                        numAsteroidDestroyed += 1
                        break
            elif x < 0 and y == 0: # left
                if (aX + x < 0):
                    continue
                for i in range(aX+x, -1, x):
                    if grid[aY][i] == '#':
                        grid[aY][i] = '.'
                        asteroidsDestroyedMap[numAsteroidDestroyed] = (i, aY)
                        numAsteroidDestroyed += 1
                        break

    return asteroidsDestroyedMap[199]

def main():
    grid = readFile("day10/sample.txt")
    numDetected, asteriod = part1(grid)
    print(numDetected, asteriod)
    asteroid = part2(asteriod, grid)
    print(asteroid[0] * 100 + asteroid[1])

main()


