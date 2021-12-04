from pathlib import Path


def main():
    # read the input
    file = Path(__file__).with_name('input.txt').open('r')

    # initialize variables
    countLines = 0
    countOnes = [0] * 12

    # process the input
    for line in file:

        # count the lines in the file in order to determine the most common bits
        countLines += 1

        # split the line into a list of characters stripping newlines at the end
        bits = list(line.replace("\n", ""))

        # count ones in the bits
        for position, value in enumerate(bits):
            countOnes[position] += int(value)

    # calculate most common bits and build gamma rate and epsilon rate
    gammaRate, epsilonRate = buildRates(countOnes, countLines)

    # show me the answer
    print(gammaRate * epsilonRate)

    file.close()


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
