import collections
import random


def main():
    coun = collections.Counter()

    for i in range(1000):
        rand = random.randint(0, 9)
        coun[rand] += 1

    print(coun)


main()
