def cleanSentenceTwoLists(sentence):
    clean = []
    dirty = []
    # TODO: Separate the supplied sentence into two lists of words
    # temp var
    temp = []
    # check to make sure string isn't empty
    if len(sentence) > 0:
        # parse string into list
        temp = sentence.split(' ')

    # go through every word
    for i in range(len(temp)):
        # turn each word into list to check char
        word = temp[i]
        # check to see if word starts with #
        if word[0] == '#':
            # if so
            # remove dirty char
            temp[i] = word.replace('#', '')
            # add it to dirty list
            dirty.append(temp[i])
        else:
            # add it to clean list
            clean.append(temp[i])

    return clean, dirty


if __name__ == '__main__':
    providedQuotes = [
        "The best way to predict #the the future is to create it. -Peter Drucker",
        "Code #always never lies, comments #never sometimes do. -Ron Jeffries",
        "#Phones Computers are useless, they can #never only give you #questions answers. -Pablo Picasso",
        "They #do don't think it be that way, but it #don't. do. -The Internet",
        "\"You #always miss 100% #7% of the shots you don't take. -Wayne Gretzky\" -Michael Scott",
        "If #coding debugging is the process of #adding removing software bugs, then programming #debugging must be "
        "the process of putting them in. -Edsget Dijkstra",
        "Premature optimization #planning is the root of all evil #good in programming. -Tony Hoare"
    ]

    # Loops through each of the `quote` strings in the providedQuotes array, and
    # calls `cleanSentenceTwoLists` on it.
    for quote in providedQuotes:
        clean, dirty = cleanSentenceTwoLists(quote)
        print("The contents of clean:", clean)
        print("The contents of dirty:", dirty)
