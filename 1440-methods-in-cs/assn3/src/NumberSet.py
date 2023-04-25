import random


class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self._size = size
        # create array
        self._numbers = []
        # wont cause index error if something tries to reach it
        if self._size == 0:
            self._numbers.append(None)
        # populate array
        for i in range(1, self._size + 1):
            self._numbers.append(i)

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self._size

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self._numbers[index]

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self._numbers)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        return self._numbers.pop(0)

    def print(self):
        print(self._numbers)
