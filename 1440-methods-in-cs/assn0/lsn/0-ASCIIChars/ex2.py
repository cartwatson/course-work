def listOfASCIIInts(charList):
    returnList = []
    # TODO: convert a list of characters into a list of ints based on ASCII

    for i in range(len(charList)):
        # convert int from intList into char
        temp = charList[i]
        temp = ord(temp)
        # add char to list
        returnList.append(temp)

    return returnList


if __name__ == '__main__':
    provided = ["A", "B", "c", "1", "-", "_", "~", " ", "z", "Y", "x"]
    provided2 = "Will you pass this test too?"

    print(listOfASCIIInts(provided))
    print(listOfASCIIInts(provided2))
