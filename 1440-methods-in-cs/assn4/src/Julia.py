#!/bin/env python3

# Julia Set Visualizer

from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, dictionary):
        self.__config = dictionary
        self.__maxIterations = dictionary["iterations"]

    def count(self, z):
        """Return the color of the current pixel within the Julia set"""
        c = complex(self.__config["creal"], self.__config["cimag"])

        for i in range(self.__maxIterations):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.__maxIterations - 1

    def getConfig(self):
        return self.__config
