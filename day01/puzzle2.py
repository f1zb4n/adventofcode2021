from pathlib import Path


def main():
    # read the input
    file = Path(__file__).with_name('input.txt').open('r')

    # initialize variables
    increaseCounter = 0
    slidingWindowQueue = []

    # process the input
    for line in file:

        # convert input line from string to int
        currentValue = int(line)

        # put new value into the queue (at the end)
        slidingWindowQueue.append(currentValue)

        if (len(slidingWindowQueue) == 4):

            # we have enough values to compare current and previous sliding window
            currentSum = buildCurrentSum(slidingWindowQueue)
            previousSum = buildPreviousSum(slidingWindowQueue)

            if (currentSum > previousSum):

                # current sliding window sum is greater than the previous one
                increaseCounter += 1

            # remove the value at the front of the queue as we do not need it anymore
            slidingWindowQueue.pop(0)

    # show me the answer
    print(increaseCounter)

    file.close()


def buildCurrentSum(slidingWindowQueue):
    return slidingWindowQueue[1] + slidingWindowQueue[2] + slidingWindowQueue[3]


def buildPreviousSum(slidingWindowQueue):
    return slidingWindowQueue[0] + slidingWindowQueue[1] + slidingWindowQueue[2]


if __name__ == "__main__":
    main()
