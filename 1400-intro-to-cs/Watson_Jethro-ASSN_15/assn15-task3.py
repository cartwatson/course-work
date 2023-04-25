from gronkyutil import deck
import gronkyutil


def bubbleSort(inputList):
    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(len(inputList) - 1):
            if inputList[i].getID() > inputList[i + 1].getID():
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True


def insertionSort(inputList):
    for i in range(1, len(inputList)):
        currElement = inputList[i]
        j = i - 1
        while j >= 0 and inputList[j].getValue() > currElement.getValue():
            inputList[j + 1] = inputList[j]
            j -= 1

        inputList[j + 1] = currElement


def binary_search(input_list, key):
    low = 0
    high = len(input_list) - 1
    while high >= low:
        mid = (high + low) // 2
        temp = [input_list[mid].getValue(), input_list[mid].getPaw(), input_list[mid].getCoin()]
        if key == temp:
            return mid
        elif key < temp:
            high = mid - 1
        elif key > temp:
            low = mid + 1

    return -1


def main():
    print("Welcome to Gronky!")
    print("Your hand will now be generated.")
    # create deck
    pack = deck()
    # deal 30 cards
    hand = list()
    pack.generate_deck()
    pack.shuffle()
    for i in range(30):
        hand.append(pack.draw())
    # show menu
    selectQuit = False
    while not selectQuit:
        menu = eval(input("1) Sort by Value\n2) Sort by ID\n3) Find card\n4) New hand\n5) Quit\nSelection: "))
        # sort by value  (insertion sort function)
        if menu == 1:
            insertionSort(hand)
            for i in range(30):
                cardID = hand[i].getID()
                cardInfo = gronkyutil.convertIDToCard(cardID)
                print("{} of {} {}".format(cardInfo[0], cardInfo[1], cardInfo[2]))
            print("")   # new line

        # sort by ID     (bubble function)
        if menu == 2:
            bubbleSort(hand)
            hand.reverse()
            for i in range(30):
                cardID = hand[i].getID()
                cardInfo = gronkyutil.convertIDToCard(cardID)
                print("{} of {} {}".format(cardInfo[0], cardInfo[1], cardInfo[2]))
            print("")  # new line

        # find card      (user inserts criteria, then check to see if in hand)
        if menu == 3:
            reqVal = eval(input("Requested Value: "))
            reqPaw = input("Requested Hand: ")
            reqCoin = input("Requested Coin: ")
            cardID = gronkyutil.convertCardToValue(reqVal, reqPaw, reqCoin)
            cardList = [reqVal, reqPaw, reqCoin]
            result = binary_search(hand, cardList)
            if result == -1:
                print("No match found...\n")
            else:
                print("Match found!")
                cardInfo = gronkyutil.convertIDToCard(cardID)
                print("{} of {} {}".format(cardInfo[0], cardInfo[1], cardInfo[2]))
            print("")

        # new hand       (shuffle deck)
        if menu == 4:
            # deal 30 cards
            hand.clear()
            pack = deck()
            pack.shuffle()
            for i in range(30):
                hand.append(pack.draw())
            print("\nNew hand\n")

        # quit
        if menu == 5:
            print("Thanks for playing!")
            selectQuit = True


main()
