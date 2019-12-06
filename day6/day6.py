def readFile(fileName):
    orbitMap = dict()
    file = open(fileName, "r")
    lines = [line.rstrip() for line in file.readlines()]
    file.close()
    for orbit in lines:
        target, source = orbit.split(')')
        if source not in orbitMap:
            orbitMap[source] = target
    return orbitMap

def part1(orbitMap):
    totalOrbits = 0
    for source in orbitMap.keys():
        nextOrbit = source
        while nextOrbit in orbitMap:
            totalOrbits += 1
            nextOrbit = orbitMap[nextOrbit]
    return totalOrbits

def calculateOrbitTrailFromSource(nextOrbit, orbitMap):
    orbitTrail = []
    while nextOrbit in orbitMap:
        orbitTrail.append(nextOrbit)
        nextOrbit = orbitMap[nextOrbit]
    return orbitTrail

def part2(orbitMap):
    # find orbits for YOU and SAN
    youOrbitTrail = calculateOrbitTrailFromSource(orbitMap["YOU"], orbitMap)[::-1]
    sanOrbitTrail = calculateOrbitTrailFromSource(orbitMap["SAN"], orbitMap)[::-1]

    # diff between two trails
    uniqueYouOrbits = [o for o in youOrbitTrail if o not in sanOrbitTrail]
    uniqueSanOrbits = [o for o in sanOrbitTrail if o not in youOrbitTrail]

    return len(uniqueYouOrbits) + len(uniqueSanOrbits)

def main():
    orbitMap = readFile("day6/input.txt")
    count = part1(orbitMap)
    print(count)

    orbitMap = readFile("day6/input.txt")
    count = part2(orbitMap)
    print(count)

main()