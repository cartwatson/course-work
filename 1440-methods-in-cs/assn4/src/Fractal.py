class Fractal():
    def __init__(self, dictionary):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

    def count(self, complexNumber):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def getConfig(self):
        raise NotImplementedError("Reference dictionary before creation")

