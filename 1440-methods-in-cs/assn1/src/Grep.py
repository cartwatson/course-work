def grep(args):
    """print lines that match patterns"""
    # check for flag
    flag = False
    if args[0] == "-v":
        # remove flag
        args.pop(0)
        # change flag state
        flag = True
    # grab pattern
    pattern = args[0]
    args.pop(0)
    # open file
    file = open(args[0], "r")
    # find pattern in line and print line
    # iterate through lines
    for line in file:
        if pattern in line and not flag:
            print(line, end="")
        if pattern not in line and flag:
            print(line, end="")
    # close file
    file.close()
