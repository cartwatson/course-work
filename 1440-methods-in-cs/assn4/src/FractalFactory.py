from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot3 import Mandelbrot3


class FractalFactory():
    def __init__(self):
        self.__fractalType = ""

    def makeFractal(self, dictionary):
        # default handled in main.py
        self.__fractalType = dictionary["type"]
        # determine fractal type
        if self.__fractalType == "julia":
            return Julia(dictionary)
        elif self.__fractalType == "mandelbrot":
            return Mandelbrot(dictionary)
        elif self.__fractalType == "mandelbrot3":
            return Mandelbrot3(dictionary)
        else:
            raise NotImplementedError("Invalid fractal type")
