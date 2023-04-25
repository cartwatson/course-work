def listOfChars(intList):
    returnList = []
    # TODO: Append to characters to `list`

    for i in range(len(intList)):
        # convert int from intList into char
        temp = intList[i]
        temp = chr(temp)
        # add char to list
        returnList.append(temp)

    return returnList


if __name__ == '__main__':
    provided = [
        65,
        32,
        115,
        104,
        111,
        114,
        116,
        32,
        115,
        101,
        110,
        116,
        101,
        110,
        99,
        101,
        46
    ]

    result = listOfChars(provided)

    # Turns the list `result` into a string `resultStr`
    resultStr = ""
    for char in result:
        resultStr += char
    print(resultStr)
