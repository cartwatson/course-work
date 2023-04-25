def cut(args):
    """remove sections from each line of files"""
    # init column
    column = 1
    # check flag and number
    if args[0] == "-f":
        # remove flag
        args.pop(0)
        # validate number proceeding flag
        validNumber(args[0])
        column = int(args[0])
        args.pop(0)


    # iterate through arguments
    for i in args:
        # open file
        file = open(i, "r")
        for j in file.readlines():
            wordlist = j.split(',')
            print(wordlist[column-1])


        # close file
        file.close()


def paste(args):
    """merge lines of files"""
    # init master list
    masterList = []
    # init maxLength
    maxLen = 0
    # iterate through arguments
    for i in args:
        # open file
        file = open(i, "r")
        # create list
        listFile = []
        for i in file.readlines():
            # remove end line characters
            i = i.replace("\n", "")
            # append contents of line
            listFile.append(i)
        # dynamically adjust max
        if len(listFile) > maxLen:
            maxLen = len(listFile)
        # add list to master list
        masterList.append(listFile)
        # close file
        file.close()
    # expand lists so they're all the same size
    for j in range(len(masterList)):
        for i in range(len(masterList[j]), maxLen):
            masterList[j].append("")
    # print master list
    # init output list
    outputList = []
    # transpose masterList
    for i in range(len(masterList[0])):
        flipped = []
        for j in masterList:
            flipped.append(j[i])
        outputList.append(flipped)

    # print output list
    for i in outputList:
        iterator = 0
        for j in i:
            print(j, end="")
            # j is not last item in i
            if iterator == len(i):
                print("\n", end="")
            else:
                print(",", end="")
            iterator += 1
        print()


def validNumber(var1):
    # check ascii value
    for i in range(len(var1)):
        if  48 <= ord(var1[i]) <= 57:
            pass
        else:
            print("invalid value following flag")
            exit(1)
    return True
