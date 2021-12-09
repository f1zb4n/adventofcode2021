from pathlib import Path

from board import Board


def main():
    # read the input
    file = Path(__file__).with_name('input.txt').open('r')

    # initialize variables
    lines = file.readlines()
    drawnNumbers = []
    boards = []

    # read first line with drawn numbers
    drawnNumbers = lines.pop(0).replace('\n', '').split(",")

    # read the boards
    boards = readBoards(lines)

    # draw the numbers
    for drawnNumber in drawnNumbers:

        # mark the number on all boards
        boards = markNumberOnBoards(drawnNumber, boards)

        # check if board has bingo
        boards = checkBingo(boards, drawnNumber)

        if (len(boards) == 0):
            break

    file.close()


def readBoards(lines):
    boards = []
    board = Board()

    for line in lines:

        if (len(line) == 1):
            continue
        else:
            board.rows.append(line.replace('\n', '').split())
            if (len(board.rows) == 5):
                boards.append(board)
                board = Board()

    return boards


def markNumberOnBoards(number, boards):
    for index, board in enumerate(boards):
        boards[index] = board.markNumber(number)

    return boards


def checkBingo(boards, drawnNumber):
    unfinishedBoards = []

    for board in boards:
        bingo = board.checkBingo()

        if (bingo):
            if (len(boards) == 1):
                # show me the answer
                print("BINGO in last board!")
                print(board.toString())
                print("Drawn number: " + drawnNumber)
                sumOfUnmarkedNumbers = board.sumUnmarkedNumbers()
                print("Sum of unmarked numbers: " + str(sumOfUnmarkedNumbers))
                print(sumOfUnmarkedNumbers * int(drawnNumber))

        else:
            # add unfinished board to list
            unfinishedBoards.append(board)

    print("Unfinished boards remaining: " + str(len(unfinishedBoards)))
    return unfinishedBoards


def printBoards(boards):
    for board in boards:
        print(board.toString())


if __name__ == "__main__":
    main()
