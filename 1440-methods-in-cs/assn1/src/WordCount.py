def wc(files):
    """print newline, word, and byte counts for each file"""
    # init global counters
    lineCountGlobal = 0
    wordCountGlobal = 0
    byteCountGlobal = 0

    # iterate through args given
    for i in files:
        # open file
        file = open(i, "r")

        # read lines
        lineCount = 0
        wordCount = 0
        byteCount = 0
        for line in file.readlines():
            lineCount += 1
            lineCountGlobal += 1
            # read bytes
            for char in line:
                byteCount += 1
                byteCountGlobal += 1
                if char == " ":
                    wordCount += 1
                    wordCountGlobal += 1

        # print counters and file name
        print(str(lineCount) + " " + str(wordCount) + " " + str(byteCount) + " " + file.name)
        # close files
        file.close()

    if len(files) >= 2:
        # print counters and total
        print(str(lineCountGlobal) + " " + str(wordCountGlobal) + " " + str(byteCountGlobal) + " total")