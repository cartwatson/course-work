import os
# We import sys for the function sys.exit to exit the program at any given point
import sys


def getFileSafely(path):
    '''
    Function to safely return a file object. If `path` does not exist, the program exits by calling `sys.exit(1)`
    after warning the user
    '''
    # check file
    if os.access(path, os.F_OK):
        # if its there
        # congratulate user
        print("File Found")
        return open(path)
    else:
        # file not found
        # give error
        print("File Not Found. System will now exit.")
        sys.exit(1)
    pass

if __name__ ==\
        '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    file = getFileSafely(filename)
    # The following line should *NEVER* get executed if `filename` is invalid
    file.close()
