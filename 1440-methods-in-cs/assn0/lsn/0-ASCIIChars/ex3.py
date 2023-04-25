def scoreWord(word):
    sum = 0
    # TODO: Score the word
    for i in range(len(word)):
        # convert ascii into int
        temp = ord(word[i])
        # test to see if alphabetic
        if 65 <= temp <= 90 or 97 <= temp <= 122:
            # test to see if lower case
            if 97 <= temp <= 122:
                # if lower case make upper case
                temp -= 32
            # subtract 64 from temp to make a or A equal zero
            temp -= 65
            # add temp to sum
            sum += temp

    return sum


if __name__ == '__main__':
    provided = [
        "One",
        "oNE",
        "supercalifragilisticexpialidocious",
        "t",
        "aAaA",
        "Zap!",
        "Tr!ck3d y4!",
        "G0t it!"
    ]

    # For each word in the provided list, give the word to the function score word and print some fancy formatted output
    for word in provided:
        print(f"The score of {word} is: {scoreWord(word)}")
