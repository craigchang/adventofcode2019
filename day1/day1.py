import math

def readFile():
    file = open("day1/input.txt", "r")
    massList = [int(x) for x in file]
    file.close()
    return massList

def calculateFuel(mass):
    return math.floor(mass / 3) - 2    

def part1(massList):
    return sum([calculateFuel(mass) for mass in massList])

def part2 (massList):
    sumFuel = 0
    for mass in massList:
        sumFuelForMass = 0
        while True:
            remainingFuel = calculateFuel(mass)
            if (remainingFuel <= 0):
                break
            sumFuelForMass += remainingFuel
            mass = remainingFuel
        sumFuel += sumFuelForMass

    return sumFuel

massList = readFile()
print(part1(massList))
print(part2(massList))