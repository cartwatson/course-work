from colour import Color
from Palette import Palette


class Palette0(Palette):
    def __init__(self, size):
        stepSize = size // 9
        red = Color("red")
        blue = Color("blue")
        green = Color("green")

        self.__pal = []
        self.__pal += list(red.range_to(blue, stepSize + 1))
        self.__pal += list(blue.range_to(green, stepSize + 2))[1:]
        self.__pal += list(green.range_to(red, stepSize + 2))[1:]


    def getColor(self, count):
        if count < len(self.__pal):
            color = self.__pal[count]
            return color.get_hex_l()
        else:
            return self.__pal[len(self.__pal) - 1]
