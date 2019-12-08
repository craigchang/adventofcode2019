def getValueByParam(intCode, param, pos):
    return intCode[pos] if param == 0 else pos

def executeIntCode(intCode, inputValues, ptr = 0):
    output = [inputValues[len(inputValues)-1]]

    while(intCode[ptr] != 99):
        opcodeWithParams = intCode[ptr]
        param2 = int((opcodeWithParams % 10000) / 1000)
        param1 = int((opcodeWithParams % 1000) / 100)
        opcode = int(opcodeWithParams % 100)

        if (opcode == 1): # add
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            intCode[intCode[ptr+3]] = val1 + val2
            ptr += 4
        elif (opcode == 2): # multiply
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            intCode[intCode[ptr+3]] = val1 * val2
            ptr += 4
        elif (opcode == 3): # store input val at address
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], settings[settingIndex])
            intCode[intCode[ptr+1]] = inputValues[0]
            inputValues.pop(0)
            ptr += 2
        elif (opcode == 4): # output val from address
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            output.append(val1)
            ptr += 2
            return val1, ptr
        elif (opcode == 5): # jump if true
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            ptr = val2 if val1 != 0 else (ptr+3)
        elif (opcode == 6): # jump if false
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            ptr = val2 if val1 == 0 else (ptr+3)
        elif (opcode == 7): # less than
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            intCode[intCode[ptr+3]] = 1 if val1 < val2 else 0
            ptr += 4
        elif (opcode == 8): # less than
            #print("Instruction @", ptr, opcodeWithParams, intCode[ptr+1], intCode[ptr+2], intCode[ptr+3])
            val1 = getValueByParam(intCode, param1, intCode[ptr+1])
            val2 = getValueByParam(intCode, param2, intCode[ptr+2])
            intCode[intCode[ptr+3]] = 1 if val1 == val2 else 0
            ptr += 4

    #print(output)
    return output[len(output)-1], 99

