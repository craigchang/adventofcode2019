def readFile():
    file = open("day2/input.txt", "r")
    intCode = [int(x) for x in file.readline().split(",")]
    print(intCode)
    file.close()
    return intCode

def calculateOutput(instructionPtr, intCode):
    opcode = intCode[instructionPtr]
    pos1 = intCode[instructionPtr+1]
    pos2 = intCode[instructionPtr+2]
    posOutput = intCode[instructionPtr+3]
    intCode[posOutput] = (intCode[pos1] + intCode[pos2]) if opcode == 1 else (intCode[pos1] * intCode[pos2])
    return intCode[posOutput]

def part1(intCode):
    intCode[1] = 12 # change pos 1 to 12
    intCode[2] = 2 # change pos 2 to 2
    instructionPtr = 0

    while(intCode[instructionPtr] != 99):
        calculateOutput(instructionPtr, intCode)
        instructionPtr += 4

    return intCode[0]

def part2(originalIntCode):
    for noun in range(100):
        for verb in range(100):
            intCode = originalIntCode.copy()
            intCode[1] = noun
            intCode[2] = verb
            instructionPtr = 0
            while(intCode[instructionPtr] != 99):
                if(calculateOutput(instructionPtr, intCode) == 19690720):
                    return (noun, verb)
                instructionPtr += 4

    return intCode

def main():
    # part 1
    intCode = readFile()
    value = part1(intCode)
    print(value)

    # part 2
    originalIntCode = readFile()
    (noun, verb) = part2(originalIntCode)
    print(100 * noun + verb)

main()