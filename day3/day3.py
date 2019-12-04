import math

class Path:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

def readFile():
    # read two lines
    file = open("day3/input.txt", "r")
    line1 = file.readline().rstrip()
    line2 = file.readline().rstrip()
    file.close()

    # store path data in lists
    line1Path = []
    line2Path = []
    for path in line1.split(","):
        path = Path(path[0], int(path[1:len(path)]))
        line1Path.append(path)
    for path in line2.split(","):
        path = Path(path[0], int(path[1:len(path)]))
        line2Path.append(path)
    
    return line1Path, line2Path

def drawLinePath(line1path, grid, isLine1 = False):
    x = y = 0
    for path in line1path:
        for dist in range(path.distance):
            if (path.direction == "R"):
                x += 1
            elif (path.direction == "U"):
                y += 1
            elif (path.direction == "L"):
                x -= 1
            else:
                y -= 1

            if (x, y) not in grid:
                grid[(x, y)] = "*" if isLine1 else "#"
            elif (grid[(x, y)] == "*" and not isLine1):
                grid[(x, y)] = "X"

def calculateManhattanDistance(grid):
    samllestDistance = math.inf
    for coord, point in grid.items():
        if point == "X":
            distance = abs(coord[0]) + abs(coord[1])
            if (distance < samllestDistance):
                samllestDistance = distance
    
    return samllestDistance

def part1(line1path, line2path):
    grid = dict()
    grid[(0,0)] = "o"

    drawLinePath(line1path, grid, True)
    drawLinePath(line2path, grid)

    return calculateManhattanDistance(grid), grid
    
def getPointsWithX(grid):
    pointsWithX = []
    for k, v in grid.items():
        if v == "X":
            pointsWithX.append(k)
    return pointsWithX

def findWithFewestSteps(point, linePath, grid):
    x = y = lineSteps = stop = 0
    for path in linePath:
        for dist in range(path.distance):
            if (path.direction == "R"):
                x += 1
            elif (path.direction == "U"):
                y += 1
            elif (path.direction == "L"):
                x -= 1
            else:
                y -= 1
            lineSteps += 1
            if (point[0] == x and point[1] == y and grid[point] == "X"):
                stop = 1
                break
        if stop == 1:
            break
    return lineSteps

def part2(line1path, line2path, grid):
    pointsWithX = getPointsWithX(grid)

    smallestSteps = math.inf

    for point in pointsWithX:
        line1Steps = findWithFewestSteps(point, line1path, grid)
        line2Steps = findWithFewestSteps(point, line2path, grid)

        if (smallestSteps > line1Steps + line2Steps):
            smallestSteps = (line1Steps + line2Steps)

    return smallestSteps

def main():
    line1path, line2path = readFile()
    smallestDistance, grid = part1(line1path, line2path)
    print(smallestDistance)
    smallestSteps = part2(line1path, line2path, grid)
    print(smallestSteps)

main()
