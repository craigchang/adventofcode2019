import collections
import math

def readFile(fileName):
    f = open(fileName, "r")
    chemDict = dict()

    for line in f.readlines():
        inLine, outLine = line.rstrip().split("=>")
        inputs = inLine.rstrip().lstrip().split(", ")
        outQ, outC = outLine.rstrip().lstrip().split(" ")
        key = outC + "=" + outQ
        chemDict[key] = dict()
        
        for i in inputs:
            q, c = i.split(" ")
            q = int(q)
            chemDict[key][c] = q

    return chemDict


def getAllChemicals(results, chemDict, currentKey):
    for k,v in chemDict[currentKey].items():
        keyFork = [key for key in chemDict if (k + "=") in key][0]
        keyC, keyQ = keyFork.split("=")
        numTimes = int(v / int(keyQ))
        numTimes = numTimes+1 if numTimes == 0 else numTimes
        print(k,v, "->", keyQ, keyC, numTimes, "time(s)")
        if 'ORE' in chemDict[keyFork]:
            if keyC not in results:
                results[k] = v
            else:
                results[k] += v
        else:
            

            for i in range(0, v, int(keyQ)):
                getAllChemicals(results, chemDict, keyFork)

def getAllChemicals2(results, chemDict, currentKey, mag):
    for k,v in chemDict[currentKey].items():
        keyFork = [key for key in chemDict if (k + "=") in key][0]
        keyC, keyQ = keyFork.split("=")
        keyQ = int(keyQ)
        numTimes = int(v / keyQ)
        numTimes = numTimes+1 if numTimes == 0 else numTimes
        print(k,v, "->", keyQ, keyC, numTimes, "time(s)")
        if 'ORE' in chemDict[keyFork]:
            if keyC not in results:
                results[k] = v
                #results[k] = v
            else:
                results[k] += v
                #results[k] += v
        else:
            mag = math.ceil(v / keyQ * mag)
            for i in range(0, mag):
                getAllChemicals2(results, chemDict, keyFork, mag)
            mag = 1
    return

def main():
    chemDict = readFile("day14/sample.txt")
    # print('Chemistry dict:')
    for k,v in chemDict.items():
        print(k, ":", v)
    results = dict()



    # get chemical
    # getAllChemicals(results, chemDict, "FUEL=1")
    getAllChemicals2(results, chemDict, "FUEL=1", 1)
    
    print(results)

    totalOreAmount = 0
    for k,v in results.items():
        keyFork = [key for key in chemDict if (k + "=") in key][0]
        keyC, keyQ = keyFork.split("=")
        oreAmount = 0
        oreAmountForChem = chemDict[keyFork]['ORE']
        for i in range(0, v, int(keyQ)):
            oreAmount += oreAmountForChem
        totalOreAmount += oreAmount
        print(k, oreAmount)
    print(totalOreAmount)

main()