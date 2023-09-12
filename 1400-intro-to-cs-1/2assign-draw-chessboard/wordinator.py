class Wordinator:
    def __init__(self, var1, var2):
        self.__word1 = var1
        self.__word2 = var2

    def firstWord(self):
        if self.__word1 < self.__word2:
            print(self.__word1)
        else:
            print(self.__word2)

    def bigWord(self):
        print(self.__word1 + self.__word2)

    def wordsFactor(self):
        count = eval(input("input: "))

        print("var1" * count + "var2" * count)

    def mixWords(self):
        length1 = len(self.__word1)
        length2 = len(self.__word2)

        if length1 > length2:
            maxLength = length1
        else:
            maxLength = length2

        for i in range(maxLength):
            if i < len(self.__word2) and i < len(self.__word1):
                print(self.__word1[i], end="")
                print(self.__word2[i], end="")
            elif i < len(self.__word1):
                print(self.__word1[i], end="")
            elif i < len(self.__word2):
                print(self.__word2[i], end="")

    def middleWords(self):
        self.__chop(self.__word1)
        self.__chop(self.__word2)

    def __chop(self, var1):
        length = len(var1)
        chop = round(length / 4 + 0.01)

        newstr = ""

        for i in range(length):
            if i < chop or i > length - chop - 1:
                continue
            else:
                newstr = newstr + var1[i]
        print(newstr)

    def switchCase(self):
        self.__splitSwitchCase(self.__word1)
        self.__splitSwitchCase(self.__word2)

    def __splitSwitchCase(self, testStr):
        newStr = ""
        for i in range(len(testStr)):
            # if testStr[i] is capital
            if ord(testStr[i]) > 90:
                newStr = newStr + chr(ord(testStr[i]) - 32)
            else:
                newStr = newStr + chr(ord(testStr[i]) + 32)
        print(newStr)

    def backWordsSlice(self):
        self.__sliceReverse(self.__word1)
        self.__sliceReverse(self.__word2)

    def __sliceReverse(self, testStr):
        newStr = testStr[::-1]
        print(newStr)

    def backWordsManual(self):
        self.__manualReverse(self.__word1)
        self.__manualReverse(self.__word2)

    def __manualReverse(self, testStr):
        newstr = ""

        for i in range(len(testStr)):
            if i == 0:
                newstr = newstr + testStr[len(testStr)-1]
            else:
                newstr = newstr + testStr[-i-1]
            # newstr = newstr + testStr[-i]
        print(newstr)
