import math

def readFile(fileName):
    file = open(fileName, "r")
    data = file.readline().rstrip()
    file.close()
    return data

def createLayers(data, width, height):
    layers = []
    layerSize = int(width * height)
    for layer in range(0, len(data), layerSize):
        layers.append(data[layer:layer + layerSize])
    return layers

def part1(data, width, height):
    layers = createLayers(data, width, height)
    
    # find layer with fewest zeros
    minZero = math.inf
    layerWithMostZeros = 0
    layerIndex = 0
    for layer in layers:
        numZeros = layer.count('0')
        if numZeros <= minZero:
            minZero = numZeros
            layerWithMostZeros = layerIndex
        layerIndex += 1

    return layers[layerWithMostZeros].count('1') * layers[layerWithMostZeros].count('2')

def part2(data, width, height):
    layers = createLayers(data, width, height)

    # loop through each pixel by stacked layers
    layerSize = int(width * height)
    output = []
    for w in range(layerSize):
        stackedLayer = [layers[h][w] for h in range(0, len(layers))]
        for pixel in stackedLayer:
            if pixel == '2':
                continue
            else:
                output.append(pixel)
                break

    outputStr = "".join(output)
    for i in range(0, layerSize, width):
        print(outputStr[i:i+width])

def main():
    # part 1 sample
    # data = readFile("day8/sample.txt")
    # print(part1(data, 3, 2))

    # part 1
    data = readFile("day8/input.txt")
    print(part1(data, 25, 6))

    # part 2 sample
    # data = readFile("day8/sample2.txt")
    # print(part2(data, 2, 2))

    # part 2
    data = readFile("day8/input.txt")
    part2(data, 25, 6)

main()