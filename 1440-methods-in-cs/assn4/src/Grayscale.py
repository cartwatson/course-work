from colour import Color
from Palette import Palette


class Grayscale(Palette):
    def __init__(self, size):
        stepSize = size // 9
        black = Color("black")
        white = Color("white")

        self.__pal = list(white.range_to(black, stepSize + 1))
        self.__pal += list(black.range_to(white, stepSize + 2))[1:]
        self.__pal += list(white.range_to(black, stepSize + 2))[1:]
        self.__pal += list(black.range_to(white, stepSize + 2))[1:]
        self.__pal += list(white.range_to(black, stepSize + 2))[1:]
        self.__pal += list(black.range_to(white, stepSize + 2))[1:]
        self.__pal += list(white.range_to(black, stepSize + 2))[1:]
        self.__pal += list(black.range_to(white, stepSize + 2))[1:]

    def getColor(self, count):
        if count < len(self.__pal):
            color = self.__pal[count]
            return color.get_hex_l()
        else:
            return self.__pal[len(self.__pal) - 1]
