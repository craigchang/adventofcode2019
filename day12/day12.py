import re
from itertools import combinations
import copy
import time
import math
import functools 
  
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xV = 0
        self.yV = 0
        self.zV = 0

def readFile(fileName):
    f = open(fileName, "r")
    moonList = []
    for line in f.readlines():
        line = line.rstrip()
        x = re.search("x=-*\d+", line).group(0).split("=")[1]
        y = re.search("y=-*\d+", line).group(0).split("=")[1]
        z = re.search("z=-*\d+", line).group(0).split("=")[1]
        moonList.append(Moon(int(x),int(y),int(z)))
    return moonList

def printTimeStamp(steps, moonList):
    print("After %d steps:" %(steps))

    for m in moonList:
        print("pos=<x=%2d, y=%2d, z=%2d>, vel=<x=%2d, y=%2d, z=%2d>" % (m.x, m.y, m.z, m.xV, m.yV, m.zV))

def applyGravity(currentMoon, otherMoon):
    if currentMoon.x > otherMoon.x:
        currentMoon.xV -= 1
        otherMoon.xV += 1
    elif currentMoon.x < otherMoon.x:
        currentMoon.xV += 1
        otherMoon.xV -= 1

    if currentMoon.y > otherMoon.y:
        currentMoon.yV -= 1
        otherMoon.yV += 1
    elif currentMoon.y < otherMoon.y:
        currentMoon.yV += 1
        otherMoon.yV -= 1

    if currentMoon.z > otherMoon.z:
        currentMoon.zV -= 1
        otherMoon.zV += 1
    elif currentMoon.z < otherMoon.z:
        currentMoon.zV += 1
        otherMoon.zV -= 1
    
def applyVelocity(moonList):
    for m in moonList:
        m.x += m.xV
        m.y += m.yV
        m.z += m.zV

def calculateTotalEnergy(moonList):
    totalEnergy = 0
    for m in moonList:
        totalEnergy += ((abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.xV) + abs(m.yV) + abs(m.zV)))
    return totalEnergy

def isBackToOriginalState(moonList, moonListModified):
    for m1,m2 in zip(moonList, moonListModified):
        if not (m1.x == m2.x and m1.y == m2.y and m1.z == m2.z and m1.xV == m2.xV and m1.yV == m2.yV and m1.zV == m2.zV):
            return False
    return True

def isXPositionAndVelocityMatch(moonList, moonListModified):
    for m1,m2 in zip(moonList, moonListModified):
        if not (m1.x == m2.x and m1.xV == m2.xV):
            return False
    return True

def isYPositionAndVelocityMatch(moonList, moonListModified):
    for m1,m2 in zip(moonList, moonListModified):
        if not (m1.y == m2.y and m1.yV == m2.yV):
            return False
    return True

def isZPositionAndVelocityMatch(moonList, moonListModified):
    for m1,m2 in zip(moonList, moonListModified):
        if not (m1.z == m2.z and m1.zV == m2.zV):
            return False
    return True

def execute(moonList, limit):
    printTimeStamp(0, moonList)
    allCombos = list(combinations([m for m in range(len(moonList))], 2))
    for steps in range(1,limit+1):
        for m1,m2 in allCombos:
            applyGravity(moonList[m1], moonList[m2])
        applyVelocity(moonList)
        printTimeStamp(steps, moonList)
    return moonList

def execute2(moonListOriginal, moonList, limit):
    allCombos = list(combinations([m for m in range(len(moonList))], 2))
    steps = 0

    moonPeriods = dict() # stores number of steps

    steps = 0
    while(True):
        for m1,m2 in allCombos:
            applyGravity(moonList[m1], moonList[m2])
        applyVelocity(moonList)
        steps += 1
        if isXPositionAndVelocityMatch(moonListOriginal, moonList):
            moonPeriods[0] = steps
            break

    steps = 0
    moonList = copy.deepcopy(moonListOriginal)
    while(True):
        for m1,m2 in allCombos:
            applyGravity(moonList[m1], moonList[m2])
        applyVelocity(moonList)
        steps += 1
        if isYPositionAndVelocityMatch(moonListOriginal, moonList):
            moonPeriods[1] = steps
            break
    
    steps = 0
    moonList = copy.deepcopy(moonListOriginal)
    while(True):
        for m1,m2 in allCombos:
            applyGravity(moonList[m1], moonList[m2])
        applyVelocity(moonList)
        steps += 1
        if isZPositionAndVelocityMatch(moonListOriginal, moonList):
            moonPeriods[2] = steps
            break
            
    return moonPeriods

def main():
    moonList = readFile("day12/input.txt")
    moonList2 = copy.deepcopy(moonList)

    # part 1
    moonList = execute(moonList, 1000)
    print(calculateTotalEnergy(moonList))

    

    # part2
    moonList = copy.deepcopy(moonList2)
    start = time.process_time()
    moonPeriods = execute2(moonList2, moonList, 2772)
    end = time.process_time()
    x, y, z = moonPeriods[0], moonPeriods[1], moonPeriods[2]
    print(lcm(lcm(x,y),z))
    print(end-start)

main()

#2343387462