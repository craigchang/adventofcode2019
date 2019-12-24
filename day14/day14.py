import collections
import queue
import math

def readFile(fileName):
    f = open(fileName, "r")
    chemDict = dict()
    resultsDict = dict()

    for line in f.readlines():
        left, right = line.rstrip().split("=>")
        leftItems = left.rstrip().lstrip().split(", ")
        rightQ, rightC = right.rstrip().lstrip().split(" ")

        resultsDict[rightC] = int(rightQ)
        chemDict[rightC] = []
        for i in leftItems:
            q, c = i.split(" ")
            chemDict[rightC].append((c, int(q)))

    return chemDict, resultsDict

def calculateOreRequired(chemical, quantity, chemDict, resultsDict, leftoversDict=dict()):
    chemQueue = queue.Queue()
    oreAmount = 0

    for i in chemDict[chemical]:
        iC, iQ = i
        chemQueue.put((iC, iQ * quantity))

    while not chemQueue.empty():
        currentC, currentQ = chemQueue.get()

        if currentC == "ORE":
            oreAmount += currentQ
        else:
            if currentC not in leftoversDict:
                leftoversDict[currentC] = 0

            resultsQ = resultsDict[currentC] # get results of currentC

            if currentQ - leftoversDict[currentC] >= 0: # subtract current quantity from any leftovers
                currentQ -= leftoversDict[currentC] 
                leftoversDict[currentC] = 0 # use leftovers if quantity less than whats left over
            elif leftoversDict[currentC] - currentQ >= 0:
                leftoversDict[currentC] -= currentQ
                continue
            
            numReactions = range(0, currentQ + resultsQ, resultsQ)[-1]
            leftoversDict[currentC] += (numReactions - currentQ)

            for i in chemDict[currentC]:
                iC, iQ = i
                chemQueue.put((iC, iQ * math.ceil(currentQ / resultsQ)))
    
    return oreAmount

def calculateFuelAmount(chemDict, resultsDict):
    leftoversDict = dict()
    oreAmount = 0
    fuelAmount = 0

    while oreAmount < 1000000000000:
        if oreAmount < 900000000000:
            oreAmount += calculateOreRequired("FUEL", 10000, chemDict, resultsDict, leftoversDict)
            fuelAmount += 10000
        elif oreAmount < 999000000000:
            oreAmount += calculateOreRequired("FUEL", 100, chemDict, resultsDict, leftoversDict)
            fuelAmount += 100
        elif oreAmount < 999900000000:
            oreAmount += calculateOreRequired("FUEL", 10, chemDict, resultsDict, leftoversDict)
            fuelAmount += 10    
        else:
            oreAmount += calculateOreRequired("FUEL", 1, chemDict, resultsDict, leftoversDict)
            fuelAmount += 1
        print(oreAmount)

    return fuelAmount


def main():
    chemDict, resultsDict = readFile("day14/sample.txt")

    # part 1
    oreAmount = calculateOreRequired("FUEL", 1, chemDict, resultsDict)
    print(oreAmount)

    # part 2
    # answer gives me the right answer + 1 for some reason
    fuelAmount = calculateFuelAmount(chemDict, resultsDict)
    print(fuelAmount)

    
main()