from pathlib import Path

# read the input
file = Path(__file__).with_name('input.txt').open('r')

# process the input
increaseCounter = 0
previousValue = 9999

for line in file:
    
    # convert input line from string to int
    currentValue = int(line)

    # increase counter if value of current line is greater than the previous value
    if (currentValue > previousValue):
        increaseCounter += 1

    # remember the current value for the check in the next iteration
    previousValue = currentValue

# show me the answer
print(increaseCounter)

file.close()
