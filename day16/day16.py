import math
import copy
import functools
import operator

def readFile(fileName):
    f = open(fileName, "r")
    line = f.readline()
    f.close()
    return line

def rotateLeft(l, n):
    return l[n:] + l[:n]

def calculatePattern(signalSize, occurance=1):
    # base pattern is 0, 1, 0, -1
    pattern = [0] * occurance + [1] * occurance + [0] * occurance + [-1] * occurance
    if len(pattern) < signalSize:
        pattern *= math.ceil(signalSize / len(pattern))
    return rotateLeft(pattern,1)[0:signalSize]

def calculatePatternMap(signalSize):
    patternMap = dict() 
    for i in range(signalSize):
        patternMap[i] = calculatePattern(signalSize, i+1)
        print(i)
    return patternMap

def calculateOutputList(signalList, signalSize):
    print('begin pattern map')
    patternMap = calculatePatternMap(signalSize)
    print('finished pattern map')

    for k in range(100):
        outList = []
        for i in range(signalSize):
            outElement = functools.reduce(operator.add, [signalList[j] * patternMap[i][j] for j in range(i, signalSize, 1)])
            outElement = int(abs(outElement) % 10)
            outList.append(outElement)
        signalList = [e for e in outList]
        print(k)

    return "".join(map(str, signalList[0:8]))

def calculateOutputList2(signalList, signalSize):
    # only needs to calculate the ones due to offset
    for i in range(100):
        signalList[signalSize - 1] = 0 + signalList[signalSize - 1] % 10
        for i in range(signalSize - 2, -1, -1):
            signalList[i] = (signalList[i + 1] + signalList[i]) % 10

    return "".join(map(str,signalList))[0:8]

def main():
    # part 1
    signal = readFile("day16/input.txt")
    signalSize = len(signal)
    signalList = [int(c) for c in signal]
    outputList = calculateOutputList(signalList, signalSize)
    print(outputList)

    # part 2
    signal = readFile("day16/input.txt") * 10000
    messageOffset = signal[0:7]
    signal = signal[int(messageOffset):]
    signalSize = len(signal)
    signalList = [int(c) for c in signal]
    outputList = calculateOutputList2(signalList, signalSize)
    print(outputList)

main()