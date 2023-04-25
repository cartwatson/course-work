class cuboid:
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def __volume(self):
        return self.__side1 * self.__side2 * self.__side3

    def __add__(self, other):
        return cuboid(self.__side1 + other.__side1, self.__side2 + other.__side2, self.__side3 + other.__side3)

    def __sub__(self, other):
        if (self.__side1 - other.__side1) < 0:
            __side1 = other.__side1 - self.__side1
        else:
            __side1 = self.__side1 - other.__side1

        if (self.__side2 - other.__side2) < 0:
            __side2 = other.__side2 - self.__side2
        else:
            __side2 = self.__side2 - other.__side2

        if (self.__side3 - other.__side3) < 0:
            __side3 = other.__side3 - self.__side3
        else:
            __side3 = self.__side3 - other.__side3
        return cuboid(__side1, __side2, __side3)

    def __lt__(self, other):
        return self.__volume() < other.__volume()

    def __gt__(self, other):
        return self.__volume() > other.__volume()

    def __eq__(self, other):
        return self.__volume() == other.__volume()

    def __len__(self):
        return self.__side1 * self.__side2 * 2 + self.__side1 * self.__side3 * 2 + self.__side2 * self.__side3 * 2

    def __str__(self):
        return "Side 1: " + str(self.__side1) + "\nSide 2: " + str(self.__side2) + "\nSide 3: " + str(self.__side3) + "\nVolume: " + str(self.__volume()) + "\nSurface Area: " + str(self.__len__())