import sys
# TODO:
# import the os module to get access to os.access and os.R_OK
import os


def sendError(string=""):
    '''
Exits the program after displaying `string` as an error message. If no string
input is provided, the default message is "Error! An error was encountered, so
the program is quitting."
    '''
    # Dear Future Dev,
    # The code below is fine. Your work is not needed on `sendError`.
    # You are more than welcome to edit the string literal, especially to make
    # an angrier (but still polite) quack.
    if string == "":
        string = "Error! An error was encountered, so the program is quitting."
    print(f"""\
!!!QUACK!!!
================================================================================
{string}
================================================================================
!!!QUACK!!!
""")
    sys.exit(1)


def convertToLower(charCode):
    """
Convert the given character code to a single plain-text lowercase character.
Returns a single character.
    """
    # create reference list to get ascii chars from
    refLowerList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # return ascii char
    charCode = int(charCode)
    # validate charCode
    if charCode >= 26:
        return ''
    # return from list
    return refLowerList[charCode]


def convertToUpper(charCode):
    """
Convert the given character code to a single plain-text uppercase character.
Returns a single character.
    """
    # create reference list to get ascii chars from
    refUpperList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # return ascii char
    charCode = int(charCode)
    # validate charCode
    if charCode >= 26:
        return ''
    # return from list
    return refUpperList[charCode]


def convertToSpecialChar(charCode):
    """
Convert the given character code to a single plain-text special character.
Returns a single character.
    """
    # create separate lists for different groups
    refSpecialListA = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@']
    refSpecialListB = ['[', '\\', ']', '^', '_', '`']
    refSpecialListC = ['{', '|', '}', '~']
    # check to see what group special char is in
    # group A
    if charCode[0] == 'A':
        # remove A
        charCode = charCode.replace('A', '')
        # reference A list
        # return ascii char from list
        charCode = int(charCode)
        # validate charCode
        if charCode >= 33:
            return ''
        # return from list A
        return refSpecialListA[charCode]
    # group B
    if charCode[0] == 'B':
        # remove B
        charCode = charCode.replace('B', '')
        # reference B list
        # return ascii char from list
        charCode = int(charCode)
        # validate charCode
        if charCode >= 6:
            return ''
        # return from list B
        return refSpecialListB[charCode]
    # group C
    if charCode[0] == 'C':
        # remove C
        charCode = charCode.replace('C', '')
        # reference C list
        # return ascii char from list
        charCode = int(charCode)
        # validate charCode
        if charCode >= 4:
            return ''
        # return from list C
        return refSpecialListC[charCode]

    pass


def getFile():
    """
Prompt the user for the text file. Verify the file's existence.
Open the file and return the opened file object if the input is valid.
    """
    textFile = input("Please select a text file to parse: ")
    if os.access(textFile, os.F_OK):
        # file found
        return open(textFile)
    else:
        # file not found
        sendError("ERROR! File Not Found")


def checkFlags(flag):
    """
Check the flag given, ensuring it is valid, and returning some information
dictating which character type the flag denotes.
    """
    typeOfChar = ""

    # check to see what flag, if any is selected
    if flag == '^':
        # uppercase
        # change typeOfChar
        typeOfChar = "upper"
        # return typeOfChar
        return typeOfChar
    if flag == '_':
        # lowercase
        # change typeOfChar
        typeOfChar = "lower"
        # return typeOfChar
        return typeOfChar
    if flag == '+':
        # special char
        # change typeOfChar
        typeOfChar = "special"
        # return typeOfChar
        return typeOfChar

        # else ignore
    return typeOfChar
    pass


def decryptCharacter(character):
    """
Decrypts a single DuckieCrypt character. Returns a single character
    """
    # check flag
    typeOfChar = checkFlags(character[0])
    # decrypt based on type
    if typeOfChar == "upper":
        # eliminate flag so only char code remains
        character = character.replace('^', '')
        # return ascii char
        return convertToUpper(character)

    if typeOfChar == "lower":
        # eliminate flag so only char code remains
        character = character.replace('_', '')
        # return ascii char
        return convertToLower(character)

    if typeOfChar == "special":
        # eliminate flag so only char code remains
        character = character.replace('+', '')
        # return ascii char
        return convertToSpecialChar(character)

    if typeOfChar == "":
        # ignore
        return ''

    pass


def decryptLine(line):
    """
Decrypt a single line of DuckieCrypt. Returns a built string
    """

    # initialize output string
    output = ""
    # turn the line into a list
    lineList = line.split(' ')

    # print("len: " + str(len(lineList)))

    # call decryptChar repeatedly
    for i in range(len(lineList)):

        # DEBUG --------------------------------------------------------------------------------------------------------
        # print(str(i) + "\t", end='')
        # print(lineList[i] + "\t", end='')
        # print(str(decryptCharacter(lineList[i])))
        # --------------------------------------------------------------------------------------------------------------

        # convert char and add to output string
        output += decryptCharacter(lineList[i])
    # return output
    return output


if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()
