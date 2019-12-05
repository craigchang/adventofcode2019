validPasswordList = []

def part1(start, end):
    for n in range(start, end + 1, 1):
        numberList = [int(d) for d in str(n)]
        previousDigit = isAdjacentDouble = isDigitDecrease = 0

        for d in numberList:
            if (previousDigit > d):
                isDigitDecrease = 1
                break
            if (previousDigit == d):
                isAdjacentDouble = 1
            previousDigit = d

        # invalid password
        if not (not isAdjacentDouble or isDigitDecrease):
            validPasswordList.append(n)

    print(len(validPasswordList))

def part2(start, end):
    validPasswordList = []

    for n in range(start, end + 1, 1):
        numberList = [int(d) for d in str(n)]
        previousDigit = isAdjacentDouble = isDigitDecrease = 0
        occurances = dict()

        for d in numberList:
            if (previousDigit > d):
                isDigitDecrease = 1
                break            
            if d not in occurances:
                occurances[d] = 1
            else:
                if (previousDigit == d):
                    occurances[d] += 1
            previousDigit = d

        if 2 in occurances.values():
            isAdjacentDouble = 1

        # invalid password
        if not (not isAdjacentDouble or isDigitDecrease):
            validPasswordList.append(n)

    print(len(validPasswordList))

def main():
    part1(235741, 706948)
    part2(235741, 706948)
main()
