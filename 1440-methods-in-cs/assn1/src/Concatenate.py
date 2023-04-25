def cat(args):
    """concatenate files and print on the standard output"""
    # iterate through arguments
    for i in args:
        # open file
        file = open(i, "r")
        # print file contents
        print(file.read())
        # close file
        file.close()


def tac(args):
    """concatenate and print files in reverse"""
    # iterate through arguments
    for i in args:
        # open file
        file = open(i, "r")
        reverse = []
        #read file into list
        for line in file.readlines():
            reverse.append(line)
        # reverse list
        reverse.reverse()
        # print reversed list
        for k in reverse:
            print(k, end="")
        # close file
        file.close()
