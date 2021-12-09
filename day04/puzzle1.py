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

        # check if a board has bingo
        if (checkBingo(boards, drawnNumber)):
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
    for board in boards:
        bingo = board.checkBingo()
        if (bingo):
            # show me the answer
            print("BINGO!")
            print(board.toString())
            print("Drawn number: " + drawnNumber)
            sumOfUnmarkedNumbers = board.sumUnmarkedNumbers()
            print("Sum of unmarked numbers: " + str(sumOfUnmarkedNumbers))
            print(sumOfUnmarkedNumbers * int(drawnNumber))
            return True
    return False


def printBoards(boards):
    for board in boards:
        print(board.toString())


if __name__ == "__main__":
    main()
