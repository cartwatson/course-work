# get input from user
numberOfLines = eval(input("Input num of lines: "))

# initialize needed variables
amountOfSpace = numberOfLines
customString = ""
# start a loop from 1 to numberOfLines + 1
for i in range(1, numberOfLines + 1):
    # start white space loop
    for k in range(1, amountOfSpace):
        # determine spacer size
        for n in range(0, len(str(numberOfLines))):
            customString += " "
    amountOfSpace -= 1
    # print num
    for j in range(0, i):
        customString += str(i)
        if j != i:
            customString += " "
    print(customString, end="\n")