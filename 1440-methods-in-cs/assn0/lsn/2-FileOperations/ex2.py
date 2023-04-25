import os
import sys


def printContents1(file):
    '''
    This function will print the contents of a file object using one of the
    methods for reading the contents of files.

    `file` is an opened file object
    '''

    # taken from the test, I couldn't see info on how to read from the file
    for line in file.readlines():
        print(line, end='')
    # end of material taken from textEX0

    pass


def printContents2(file):
    '''
    This function will print the contents of a file object using one of the
    other methods for reading the contents of files.

    `file` is an opened file object
    '''

    # read lots of bytes
    lotsOfBytes = file.read(1000000)
    # print lots of bytes
    print(lotsOfBytes)
    pass


def printTwice(fileName):
    ''' TODO:
        1:  Open the file object *safely*.
            * Why don't I reuse something I've made before?
    f = a file object
        2:  Print it the first time
    printContents1(f)
        3:  Rewind the file
        4:  Print the file a second time
    printContents2(f)
        5:  Close the file
    f.close()
    '''

    # get file safely

    # code copied from ex1
    # copied due to error with print out messages
    if os.access(fileName, os.F_OK):
        # if its there
        # congratulate user
        # print("File Found")
        safeFile = open(fileName)
    else:
        # file not found
        # give error
        # print("File Not Found. System will now exit.")
        sys.exit(1)
    # end of copied code

    # first print
    printContents1(safeFile)
    # return cursor to beginning
    safeFile.seek(0)
    # second print
    printContents2(safeFile)
    # close file
    safeFile.close()
    pass

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    printTwice(filename)
