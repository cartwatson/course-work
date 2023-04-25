from Grayscale import Grayscale
from Palette0 import Palette0


class PaletteFactory():
    def __init__(self, dictionary):
        self.__config = dictionary

    def makePalette(self, paletteName):
        if paletteName == "Palette0":
            return Palette0(self.__config["iterations"])
        elif paletteName == "grayscale":
            return Grayscale(self.__config["iterations"])
        else:
            raise NotImplementedError("Invalid palette requested")