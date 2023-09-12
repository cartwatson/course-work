class Password:
    def __init__(self):
        self.__pass = None
        self.__valid = True
        self.__passList = None
        self.__digits = None

        # error messages
        self.__char8 = "must have 8 characters\n"
        self.__digits2 = "must have at least 2 digits\n"
        self.__end123 = "cannot end in 123\n"
        self.__conPass = "cannot contain \"password\"\n"
        self.__symbols = "can only consist of letters and digits\n"
        self.__errMessage = "Password is invalid for the following reasons...\n"

        # checks
        self.__symbolsInvalid = False
        self.__passwordInvalid = False

    def setPassword(self, message):
        self.__pass = message

    def getErrorMessage(self):
        return self.__errMessage

    def __sym(self, i):
        if not self.__symbolsInvalid:
            # no symbols
            if not ((65 <= ord(self.__passList[i]) <= 90) or (97 <= ord(self.__passList[i]) <= 122) or (
                    48 <= ord(self.__passList[i]) <= 57)):
                self.__errMessage += self.__symbols
                self.__valid = False
                self.__symbolsInvalid = True

    def __digitsCheck(self, i, strlen):
        # 2 or more digits
        if 48 <= ord(self.__passList[i]) <= 57:
            self.__digits += 1

        # check to see if by the end two numbers are included in the program
        if i == strlen - 1:
            if self.__digits < 2:
                self.__errMessage += self.__digits2
                self.__valid = False

    def __containsPassword(self, i):
        if not self.__passwordInvalid:
            # doesn't contain password
            if not ord(self.__passList[i + 0]) == 0 or ord(self.__passList[i + 1]) == 0 or ord(
                    self.__passList[i + 2]) == 0 or ord(self.__passList[i + 3]) == 0 or ord(
                self.__passList[i + 4]) == 0 or ord(self.__passList[i + 5]) == 0 or ord(
                self.__passList[i + 6]) == 0 or ord(self.__passList[i + 7]) == 0:
                # not containing password
                if ord(self.__passList[i + 0]) == 80 or ord(self.__passList[i + 0]) == 112:  # P
                    if ord(self.__passList[i + 1]) == 65 or ord(self.__passList[i + 1]) == 97:  # A
                        if ord(self.__passList[i + 2]) == 83 or ord(self.__passList[i + 2]) == 115:  # S
                            if ord(self.__passList[i + 3]) == 83 or ord(self.__passList[i + 3]) == 115:  # S
                                if ord(self.__passList[i + 4]) == 87 or ord(self.__passList[i + 4]) == 119:  # W
                                    if ord(self.__passList[i + 5]) == 79 or ord(self.__passList[i + 5]) == 111:  # O
                                        if ord(self.__passList[i + 6]) == 82 or ord(self.__passList[i + 6]) == 114:  # R
                                            if ord(self.__passList[i + 7]) == 50 or ord(
                                                    self.__passList[i + 7]) == 100:  # D
                                                self.__errMessage += self.__conPass
                                                self.__valid = False
                                                self.__passwordInvalid = True

    def __end123Check(self, strlen):
        # not ending in 123
        if ord(self.__passList[strlen - 3]) == 49:
            if ord(self.__passList[strlen - 2]) == 50:
                if ord(self.__passList[strlen - 1]) == 51:
                    self.__errMessage += self.__end123
                    self.__valid = False

    def __lenCheck(self, strlen):
        # 8 or more character
        if strlen < 8:
            self.__errMessage += self.__char8
            self.__valid = False

    def isValid(self):
        self.__passList = list(self.__pass)
        self.__digits = 0

        strlen = len(self.__pass)

        self.__lenCheck(strlen)

        self.__end123Check(strlen)

        for i in range(0, strlen):
            self.__sym(i)

            self.__digitsCheck(i, strlen)

            self.__containsPassword(i)

        # return validity
        if self.__valid:
            return True
        else:
            return False
