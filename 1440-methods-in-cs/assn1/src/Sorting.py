def sort(args):
    """sort lines of text files"""
    # iterate through arguments
    for i in args:
        # open file
        file = open(i, "r")
        # init list
        lineList = []
        # read all lines into list
        for i in file.readlines():
            lineList.append(i)
        # sort list
        lineList.sort()
        # print list
        for k in lineList:
            print(k, end="")
        # close file
        file.close()
