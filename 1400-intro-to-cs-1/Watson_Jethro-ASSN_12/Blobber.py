import time


class Blobber:
    def __init__(self, n: str, c: str, r: float = 50.0, h: float = 100.0):
        self.__radius = r
        self.__height = h
        self.__color = c
        self.__name = n
        self.__volumeInitial = self.__height * self.__radius * 2 * 3.14159
        self.__volumeDynamic = self.__height * self.__radius * 2 * 3.14159

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def setName(self, new):
        self.__name = new

    def setColor(self, new):
        self.__color = new

    def feedBlobber(self, food):
        self.__radius += food

    def blobberSpeak(self, startTime):
        for i in range(int(time.time() - startTime)):
            self.__radius *= .998
        self.__volumeDynamic = self.__height * self.__radius * 2 * 3.14159
        return "My name is " + self.__name + ". My current happiness level is " + \
               "{:.2f}%".format((self.__volumeDynamic / self.__volumeInitial) * 100)

    def vitalsOk(self, startTime):
        for i in range(int(time.time() - startTime)):
            self.__radius *= .998
        self.__volumeDynamic = self.__height * self.__radius * 2 * 3.14159
        if 0.9 < (self.__volumeDynamic / self.__volumeInitial) < 1.1:
            return True
        else:
            return False
