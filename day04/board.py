class Board:

    def __init__(self):
        self.rows = []

    def toString(self):
        asstring = ""
        for row in self.rows:
            asstring += repr(row)
        return asstring

    def markNumber(self, number):
        for row in self.rows:
            for index, boardNumber in enumerate(row):
                if (boardNumber == number):
                    row[index] = 'X'
                    break
        return self

    def checkBingo(self):
        # check each row
        for row in self.rows:
            rowHasBingo = True
            for boardNumber in row:
                if (boardNumber != 'X'):
                    rowHasBingo = False
                    break

            if (rowHasBingo):
                return True

        # check each column
        for columnPosition in range(len(self.rows[0])):
            columnHasBingo = True
            for row in self.rows:
                if (row[columnPosition] != 'X'):
                    columnHasBingo = False
                    break

            if (columnHasBingo):
                return True

        return False

    def sumUnmarkedNumbers(self):
        sum = 0
        for row in self.rows:
            for boardNumber in row:
                if (boardNumber != 'X'):
                    sum += int(boardNumber)

        return sum
