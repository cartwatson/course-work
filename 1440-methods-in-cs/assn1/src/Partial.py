def head(args):
    """output the first part of files"""
    # init lines to read
    lines = 10
    # check for flag
    if args[0] == '-n':
        args.pop(0)
        # check to make sure parameters are correct
        validNumber(args[0])
        lines = int(args[0])
        args.pop(0)
    # check if banners are needed
    banner = bannerCheck(args)
    # init argsIndex to keep track of pos in args for printing banner
    argsIndex = 0
    # iterate through files to print
    for i in args:
        # open file
        file = open(i, "r")
        # print banner if multiple files were given
        if banner:
            print("==> " + args[argsIndex] + " <==")
        # print file contents
        for k in range(lines):
            print(file.readline(), end="")
        # close file
        file.close()
        # increase argsIndex to use for banner
        argsIndex += 1


def tail(args):
    """output the last part of files"""
    # init lines to read
    linesPrint = 10
    # check for flag
    if args[0] == '-n':
        args.pop(0)
        # check to make sure parameters are correct
        validNumber(args[0])
        linesPrint = int(args[0])
        args.pop(0)
    # check if banners are needed
    banner = bannerCheck(args)
    # init argsIndex to keep track of pos in args for printing banner
    argsIndex = 0
    # iterate through files to print
    for i in args:
        # open file
        file = open(i, "r")
        # print banner if multiple files were given
        if banner:
            print("==> " + args[argsIndex] + " <==")
        # read and print last part of file
        linesList = []
        # read all lines into list
        for i in file.readlines():
            linesList.append(i)
        # print out last section of lines
        for k in range(len(linesList) - linesPrint, len(linesList)):
            print(linesList[k], end="")
        # close file
        file.close()
        # increase argsIndex to use for banner
        argsIndex += 1


def validNumber(var1):
    # check ascii value
    for i in range(len(var1)):
        if  48 <= ord(var1[i]) <= 57:
            pass
        else:
            print("invalid value following flag")
            exit(1)
    return True


def bannerCheck(args):
    # decide if banner is necessary
    if len(args) >= 2:
        return True
    else:
        return False
