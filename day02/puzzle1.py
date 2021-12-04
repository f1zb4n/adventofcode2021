from pathlib import Path

# read the input
file = Path(__file__).with_name('input.txt').open('r')

# initialize variables
horizontalPosition = 0
depth = 0

# process the input
for line in file:

    # split the input string into command and value
    splitted = line.split(" ")
    command = splitted[0]
    value = int(splitted[1])

    # execute command
    if ("forward" == command):
        horizontalPosition += value

    if ("down" == command):
        depth += value

    if ("up" == command):
        depth -= value

# show me the answer
print(horizontalPosition * depth)

file.close()
