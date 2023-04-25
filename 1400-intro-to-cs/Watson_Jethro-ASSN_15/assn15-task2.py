List = list()
count = 0
sumVal = 0

done = False
while not done:
    num = input("Enter a number: ")
    if num == "":
        done = True
    else:
        List.append(eval(num))
        count += 1

# max value code
for i in range(count - 1):
    swap = True
    while swap:
        swap = False
        for j in range(len(List) - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                swap = True

maxVal = List[count - 1]

# sum value code
for i in range(count):
    sumVal += List[i]

# average value code
aveVal = sumVal / count

# display stats
print("Number of values entered: " + str(count))
print("Maximum Value: " + str(maxVal))
print("Minimum Value: " + str(min(List)))
print("Sum of all values: " + str(sumVal))
print("Average value: " + str(aveVal))