#!/bin/env python3

# Mandelbrot Set Visualizer

from Fractal import Fractal

class Mandelbrot(Fractal):
    def __init__(self, dictionary):
        self.__config = dictionary
        self.__maxIterations = dictionary["iterations"]

    def count(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0)

        for i in range(self.__maxIterations):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.__maxIterations - 1

    def getConfig(self):
        return self.__config
