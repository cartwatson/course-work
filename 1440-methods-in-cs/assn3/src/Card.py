import sys

import NumberSet


class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self._idnum = idnum
        self._size = size
        self._numberSet = numberSet
        self._data = []
        # populate data
        # if even
        if self._size % 2 == 0:
            for i in range(self._size):
                tempArray = []
                for j in range(self._size):
                    tempArray.append(self._numberSet.getNext())
                self._data.append(tempArray)
        # if odd
        else:
            for i in range(self._size):
                tempArray = []
                for j in range(self._size):
                    # if middle square add free instead of data
                    if i == int(self._size / 2) and j == int(self._size / 2):
                        tempArray.append("Free!")
                    else:
                        tempArray.append(self._numberSet.getNext())
                self._data.append(tempArray)

    def getId(self):
        """Return an integer: the ID number of the card"""
        return self._idnum

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self._size

    def print(self, file=sys.stdout):
        """void function: Prints a card to the screen or to an open file object"""
        print("Card #" + str(self._idnum + 1), file=file)
        if self._size % 2 == 0:
            self._printEven(file)
        else:
            self._printOdd(file)

    def _printOdd(self, file):
        for i in range(self._size):
            print(("+--" + "-" * 5) * self._size + "+", file=file) # always 5 '-'s because of "Free!"
            for j in range(self._size):
                # print single number
                frontSpace = 1
                backSpace = 1
                # adjust spaces for "Free!"
                if self._data[i][j] == "Free!":
                    print("|" + " " + self._data[i][j] + " ", end="", file=file)
                else: # compute spaces as normal
                    if self._numberSet.getSize() < 100:
                        frontSpace += 2
                        backSpace += 1
                        # compute front and back space
                        frontSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                        if len(str(self._data[i][j])) > len(str(self._numberSet.getSize())) - 1:
                            backSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                    else: # handle when size > 100
                        frontSpace += 1
                        backSpace += 1
                        # compute front and back space
                        frontSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                        if len(str(self._data[i][j])) > len(str(self._numberSet.getSize())) - 1:
                            backSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                    # print front bar, front spaces, number, and backSpaces
                    print("|" + " " * frontSpace + str(self._data[i][j]) + " " * backSpace, end="", file=file)
            print("|", file=file)
        print(("+--" + "-" * 5) * self._size + "+", file=file)

    def _printEven(self, file):
        for i in range(self._size):
            print(("+--" + "-" * len(str(self._numberSet.getSize()))) * self._size + "+", file=file)
            for j in range(self._size):
                # print single number
                frontSpace = 1
                backSpace = 1
                # compute front and back space
                frontSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                if len(str(self._data[i][j])) > len(str(self._numberSet.getSize())) - 1:
                    backSpace += len(str(self._numberSet.getSize())) - len(str(self._data[i][j]))
                # print front bar, front spaces, number, and backSpaces
                print("|" + " " * frontSpace + str(self._data[i][j]) + " " * backSpace, end="", file=file)
            print("|", file=file)
        print(("+--" + "-" * len(str(self._numberSet.getSize()))) * self._size + "+", file=file)