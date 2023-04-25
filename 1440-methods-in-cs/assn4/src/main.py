import sys
from ImagePainter import ImagePainter
from FractalFactory import FractalFactory
from PaletteFactory import PaletteFactory

def main():
    # define dict
    configDict = {}

    # handle default and custom conditions
    if len(sys.argv) < 2:
        # fractal not given, palette not given
        fileName = "mandelbrot"
        configDict = {
            "type": "mandelbrot",
            "pixels": 640,
            "centerx": 0.0,
            "centery": 0.0,
            "axislength": 4.0,
            "iterations": 100
        }
        paletteName = "Palette0"
    elif len(sys.argv) < 3:
        # fractal given, palette not given
        fileName = sys.argv[1]
        paletteName = "Palette0"
        configDict = makeDict(fileName)
    else:
        # fractal given, palette given
        fileName = sys.argv[1]
        paletteName = sys.argv[2]
        configDict = makeDict(fileName)

    # If missing field raise RuntimeError
    requiredFields = ["type", "centerx", "centery", "axislength", "pixels", "iterations"]
    if configDict["type"] == "julia" or configDict["type"] == "burningshipjulia":
        requiredFields.append("creal")
        requiredFields.append("cimag")
    # check fields
    for i in configDict.keys():
        if i in requiredFields:
            continue
        else:
            raise NotImplementedError("Invalid fractal configuration file")

    # pick fractal from factory
    factory = FractalFactory()
    fractal = factory.makeFractal(configDict)

    pFactory = PaletteFactory(configDict)
    palette = pFactory.makePalette(paletteName)

    # feed fractal and palette into image painter
    painter = ImagePainter(fractal, palette, fileName)
    painter.createWindow()

def makeDict(fileName):
    config = open(fileName)
    # make config file into dictionary
    configDict = {}
    for line in config:
        if str(line[0]) == "#" or str(line[0]) == "\n":
            continue
        line = line.strip("\n")
        line = line.replace(" ", "")
        line = line.lower()
        keyValuePair = tuple(line.split(":"))
        # convert types correctly
        if keyValuePair[0] == "type":
            try:
                configDict[keyValuePair[0]] = keyValuePair[1]
            except:
                raise NotImplementedError("Invalid fractal configuration file")
        elif keyValuePair[0] == "centerx" or keyValuePair[0] == "centery" or \
                keyValuePair[0] == "axislength" or keyValuePair[0] == "cimag" or \
                keyValuePair[0] == "creal":
            try:
                configDict[keyValuePair[0]] = float(keyValuePair[1])
            except:
                raise NotImplementedError("Invalid fractal configuration file")
        elif keyValuePair[0] == "iterations" or keyValuePair[0] == "pixels":
            try:
                configDict[keyValuePair[0]] = int(keyValuePair[1])
            except:
                raise NotImplementedError("Invalid fractal configuration file")
        else: # if key not correct
            raise NotImplementedError("Invalid fractal configuration file")

    return configDict



main()