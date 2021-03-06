def readFile(fileName):
    file = open(fileName, "r")
    intCode = [int(x) for x in file.readline().split(",")]
    file.close()
    return intCode

def resize(intCode, pos, param = 0):
    if len(intCode) <= pos:
        for x in range(len(intCode), pos + 1):
            intCode.append(0)

def getValueByParam(intCode, param, pos, relativeBase, write=0):
    resize(intCode, pos, param)

    if param == 0: # position mode
        if write == 0:
            return intCode[pos]
        else:
            return pos
    elif param == 1: # immediate mode
        return pos
    elif param == 2: # relative mode
        if write == 0:
            return intCode[relativeBase + pos]
        else:
            return relativeBase + pos
    else:
        raise Exception('Error')

    return intCode[pos] if param == 0 else pos

def execute(intCode, inputVal):
    ptr = 0
    output = []
    relativeBase = 0

    while(intCode[ptr] != 99):
        opcodeWithParams = intCode[ptr]
        param3 = int((opcodeWithParams % 100000) / 10000)
        param2 = int((opcodeWithParams % 10000) / 1000)
        param1 = int((opcodeWithParams % 1000) / 100)
        opcode = int(opcodeWithParams % 100)

        if (opcode == 1): # add
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            val3 = getValueByParam(intCode, param3, intCode[ptr+3], relativeBase, 1)
            intCode[val3] = val1 + val2
            ptr += 4
        elif (opcode == 2): # multiply
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            val3 = getValueByParam(intCode, param3, intCode[ptr+3], relativeBase, 1)
            intCode[val3] = val1 * val2
            ptr += 4
        elif (opcode == 3): # store input val at address
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase, 1)
            intCode[val1] = inputVal
            ptr += 2
        elif (opcode == 4): # output val from address
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            output.append(val1)
            ptr += 2
        elif (opcode == 5): # jump if true
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            ptr = val2 if val1 != 0 else (ptr+3)
        elif (opcode == 6): # jump if false
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            ptr = val2 if val1 == 0 else (ptr+3)
        elif (opcode == 7): # less than
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            val3 = getValueByParam(intCode, param3, intCode[ptr+3], relativeBase, 1)
            intCode[val3] = 1 if val1 < val2 else 0
            ptr += 4
        elif (opcode == 8): # equal to
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            val2 = getValueByParam(intCode, param2, intCode[ptr+2], relativeBase)
            val3 = getValueByParam(intCode, param3, intCode[ptr+3], relativeBase, 1)
            intCode[val3] = 1 if val1 == val2 else 0
            ptr += 4
        elif (opcode == 9): # change relative base
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1], relativeBase)
            relativeBase += val1
            ptr += 2

    return output

def main():
    # intCode = readFile("day9/sample.txt")
    # output = execute(intCode, 1)
    # print(output)
    # print(output[len(output)-1])

    # intCode = readFile("day9/sample2.txt")
    # output = execute(intCode, 1)
    # print(output)
    # print(len(str(output[0])))

    # intCode = readFile("day9/sample3.txt")
    # output = execute(intCode, 1)
    # print(output)
    # print(output[len(output)-1])

    intCode = readFile("day9/input.txt")
    output = execute(intCode, 1)
    print(output[len(output)-1])

    intCode = readFile("day9/input.txt")
    output = execute(intCode, 2)
    print(output[len(output)-1])

main()