import math
from itertools import permutations
import intCodeEngine

def readFile(fileName):
    file = open(fileName, "r")
    intCode = [int(x) for x in file.readline().split(",")]
    file.close()
    return intCode

def getMaxOutputSignal(intCode):
    newIntCode = intCode.copy()
    maxSignal = 0

    allPossibleSettings = list(permutations(range(0,5)))

    for settings in allPossibleSettings:
        inputSignal = 0
        for phase in [int(x) for x in settings]:
            output = intCodeEngine.executeIntCode(newIntCode, [phase, inputSignal])
            newIntCode = intCode.copy()
            inputSignal = output[0]
        if maxSignal < output[0]:
            maxSignal = output[0]
    return maxSignal

def getMaxOutputSignalFeedbackLoop(intCode):
    maxSignal = 0

    for settings in list(permutations(range(5,10))):
        intCodeMap = [intCode.copy(), intCode.copy(), intCode.copy(), intCode.copy(), intCode.copy()] 
        intCodeSavedIndexMap = [0] * 5
        intCodeMapIndex = 0
        inputValues = [settings[0], 0]
        inputSignal = 0
        settingIndex = 0
        index = 0

        while (index != 99):
            output, index = intCodeEngine.executeIntCode(intCodeMap[intCodeMapIndex], inputValues, intCodeSavedIndexMap[intCodeMapIndex])
            
            settingIndex += 1
            if (settingIndex < 5):
                inputValues.append(settings[settingIndex])
                inputValues.append(output)
            else:
                inputValues.append(output)
            
            intCodeSavedIndexMap[intCodeMapIndex] = index

            intCodeMapIndex += 1
            if (intCodeMapIndex == 5):
                intCodeMapIndex = 0
            
            print(output)
        
        if maxSignal < output:
            maxSignal = output
    return maxSignal

def main():
    # part 1
    intCode = readFile('day7/input.txt')
    print(getMaxOutputSignal(intCode))

    # part 2
    intCode = readFile('day7/input.txt')
    # print(getMaxOutputSignalFeedbackLoop(intCode))

    # intCode = readFile('day7/sample2Part2.txt')
    # print(test2(intCode, [9,7,8,5,6]))

    #print(getMaxOutputSignal(intCode, 1))

main()