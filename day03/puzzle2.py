from pathlib import Path


def main():
    # read the input
    file = Path(__file__).with_name('input.txt').open('r')

    # initialize variables

    # read the file
    lines = file.readlines()

    # determine oxygen generator rating
    matchingValues = lines
    bitPosition = 0
    while len(matchingValues) > 1:
        mostCommonValue = findMostCommonValue(matchingValues, bitPosition)
        matchingValues = filterAtPosition(
            matchingValues, bitPosition, mostCommonValue)
        bitPosition += 1

    oxygenGeneratorRating = int(matchingValues[0], 2)

    # co2 scrubber rating
    matchingValues = lines
    bitPosition = 0
    while len(matchingValues) > 1:
        leastCommonValue = findLeastCommonValue(matchingValues, bitPosition)
        matchingValues = filterAtPosition(
            matchingValues, bitPosition, leastCommonValue)
        bitPosition += 1

    co2ScrubberRating = int(matchingValues[0], 2)

    # show me the answer
    print(oxygenGeneratorRating * co2ScrubberRating)

    file.close()


def findMostCommonValue(lines, bitPosition):
    countOnes = 0
    for line in lines:
        # split the line into a list of characters stripping newlines at the end
        bits = list(line.replace("\n", ""))
        countOnes += int(bits[bitPosition])

    if (countOnes >= len(lines) / 2):
        return 1
    else:
        return 0


def findLeastCommonValue(lines, bitPosition):
    countOnes = 0
    for line in lines:
        # split the line into a list of characters stripping newlines at the end
        bits = list(line.replace("\n", ""))
        countOnes += int(bits[bitPosition])

    if (countOnes < len(lines) / 2):
        return 1
    else:
        return 0


def filterAtPosition(matchingValues, bitPosition, mostCommonValue):
    remainingValues = []
    for line in matchingValues:
        bits = list(line.replace("\n", ""))
        if (int(bits[bitPosition]) == mostCommonValue):
            remainingValues.append(line)
    return remainingValues


def buildRates(countOnes, countLines):
    gammaRateBinary, epsilonRateBinary = "", ""

    for value in countOnes:
        if (value > countLines / 2):
            gammaRateBinary += "1"
            epsilonRateBinary += "0"
        else:
            gammaRateBinary += "0"
            epsilonRateBinary += "1"

    # transform binary values into decimal values
    return (int(gammaRateBinary, 2), int(epsilonRateBinary, 2))


if __name__ == "__main__":
    main()
