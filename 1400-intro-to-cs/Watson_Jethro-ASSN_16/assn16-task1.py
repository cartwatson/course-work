import time
from card import Card
from deck import Deck


# for debug
def printList(myList):
    for a in myList:
        print(a)
    print("DONE\n")


def calcHandTotal(myList):
    # first three elements of list are balance and bet and total
    # rest are cards
    total = 0
    cardValues = []
    handSize = len(myList) - 3
    # add all values to a list
    for j in range(handSize):
        cardValues.append(myList[j + 3].getCardValue())
    # sort list of all values in descending order
    cardValues.sort(reverse=True)
    for i in range(len(cardValues)):
        if cardValues[i] == 1:  # deal with aces
            if total + 11 <= 21:  # add as eleven when there is space
                total += 11
            else:  # add as one when adding as 11 would cause bust
                total += 1
        if cardValues[i] >= 10:  # add face cards as a ten
            total += 10
        else:  # add card normally
            if cardValues != 1: # dont add an ace twice
                total += cardValues[i]
    return total


def main():
    # initialize player info list
    playerInfo = []
    # get playerCount and validate input
    playerCount = 0
    while playerCount < 1 or playerCount > 5:
        playerCount = eval(input("Enter number of players (maximum of 5): "))
        if playerCount < 1 or playerCount > 5:
            print("Please enter valid number of players.")
            playerCount = eval(input("Enter number of players (maximum of 5): "))

    # initialize empty lists for players
    # first player is dealer
    playerInfo.append([])
    # following players are added
    for i in range(playerCount):
        playerInfo.append([])

    # initialize balances
    # initialize dealer balance and bet(N/A)
    playerInfo[0].append("N/A")
    playerInfo[0].append("N/A")
    # initialize player balance
    for i in range(playerCount):
        playerInfo[i + 1].append(100)

    # start game
    playing = True
    while playing:
        # get bets
        for i in range(playerCount):
            print("Current balance for player {} is: {}".format(i+1, playerInfo[i + 1][0]))
            # get bet and validate input
            bet = 0
            while bet > playerInfo[i + 1][0] or bet < 5:
                bet = eval(input("Enter bet amount (min $5): "))
                if bet > playerInfo[i + 1][0] or bet < 5:
                    print("Please enter valid bet.")
                    bet = eval(input("Enter bet amount (min $5): "))
            playerInfo[i + 1].append(bet)

        # initialize spot for total
        for i in range(playerCount + 1):
            playerInfo[i].append(0)

        # Deal the cards
        # generate deck
        deck = Deck()
        # deal cards to dealer and players
        for j in range(2):
            # give all players one card
            for i in range(1, playerCount + 1):
                playerInfo[i].append(deck.draw())
            # give dealer card
            playerInfo[0].append(deck.draw())
        # show dealers second card
        print("Dealer's second card is a " + str(playerInfo[0][3]))
        # print new line
        print("")

        # player action
        for i in range(playerCount):
            handSize = 2
            busted = False
            while not busted:
                # print hand
                print("Player {}'s hand".format(i+1))
                for j in range(handSize):
                    print(str(playerInfo[i + 1][j + 3]))
                # display menu and validate input
                menu = 0
                while menu > 2 or menu < 1:
                    menu = eval(input("1) Hit\n2) Hold\nSelection: "))
                    if menu > 2 or menu < 1:
                        print("Please enter valid selection.")
                        menu = eval(input("1) Hit\n2) Hold\nSelection: "))
                # take action based on menu
                # hit
                if menu == 1:
                    # add card
                    playerInfo[i + 1].append(deck.draw())
                    # increase handSize to always count and display all cards
                    handSize += 1
                    # display card
                    print("You drew a " + str(playerInfo[i + 1][handSize+2]) + "\n")
                    # calculate total
                    playerInfo[i + 1][2] = calcHandTotal(playerInfo[i + 1])
                    # check if busted
                    if playerInfo[i + 1][2] > 21:
                        print("You busted!")
                        # exit loop and move to next player
                        busted = True
                # hold
                if menu == 2:
                    # exit loop and move to next player
                    print("You held.")
                    busted = True
            playerInfo[i + 1][2] = calcHandTotal(playerInfo[i + 1])

        # dealer's turn
        # print dealer's cards
        print("The dealer's cards are...")
        print(str(playerInfo[0][3]))
        print(str(playerInfo[0][4]))
        # dealer total
        dealerTotal = calcHandTotal(playerInfo[0])

        # reset handSize for dealer use
        handSize = 2
        # dealer's actions
        while dealerTotal < 17:
            # dealer hits
            time.sleep(1)
            playerInfo[0].append(deck.draw())
            print("The dealer hits.")
            # increment handSize
            handSize += 1
            # display dealers card
            print("The dealer drew " + str(playerInfo[0][handSize + 2]))
            # recalculate total
            dealerTotal = calcHandTotal(playerInfo[0])
            # check if busted
            if dealerTotal > 21:
                print("The dealer busted!")
                # replace first card with "Busted"
                playerInfo[0][2] = dealerTotal
            # recalculate total
            dealerTotal = calcHandTotal(playerInfo[0])
            playerInfo[0][2] = dealerTotal
        # the dealer holds
        if 17 <= dealerTotal <= 21:
            print("The dealer holds.")
            playerInfo[0][2] = dealerTotal

        # determine winners
        # dealer busts
        if dealerTotal > 21:
            for i in range(playerCount):
                # check to see if player stayed under 21
                if playerInfo[i + 1][2] <= 21:
                    playerInfo[i + 1][2] = "Win"
                elif playerInfo[i + 1][2] > 21:  # player did bust
                    playerInfo[i + 1][2] = "Lost"
        # dealer doesn't bust
        if dealerTotal <= 21:
            for i in range(1, playerCount + 1):
                # check for tie
                if playerInfo[i][2] == dealerTotal and playerInfo[i][2] <= 21:
                    playerInfo[i][2] = "Tie"

                # check for win
                elif dealerTotal < playerInfo[i][2] and playerInfo[i][2] <= 21:
                    playerInfo[i][2] = "Win"

                # check for loss
                elif playerInfo[i][2] < dealerTotal or playerInfo[i][2] > 21:
                    playerInfo[i][2] = "Lost"

        # award bets
        for i in range(playerCount):
            # winners
            if playerInfo[i + 1][2] == "Win":
                # add bet to balance
                playerInfo[i + 1][0] += playerInfo[i + 1][1]
                print("Player {} wins!\nPlayer {}'s new balance is: {}".format(i + 1, i + 1, playerInfo[i +1][0]))
            # losers
            if playerInfo[i + 1][2] == "Lost":
                # subtract bet from balance
                playerInfo[i + 1][0] -= playerInfo[i + 1][1]
                print("Player {} Loss!\nPlayer {}'s new balance is: {}".format(i + 1, i + 1, playerInfo[i + 1][0]))
            # fools who tied
            if playerInfo[i + 1][2] == "Tie":
                # do nothing with bet or balance
                print("Player {} tied!\nPlayer {}'s balance is: {}".format(i + 1, i + 1, playerInfo[i + 1][0]))

        # ask if continue playing
        playMenu = input("Would you like to continue playing? (Y/N) \nSelection: ").upper()
        if playMenu == "Y":
            # set up for next game
            # dealer
            for i in range(2, len(playerInfo[0])):
                del playerInfo[0][2]
            # players
            removedPlayers = []
            for k in range(1, playerCount + 1):
                # remove broke players
                if playerInfo[k][0] == 0:
                    print("Player {} has been removed.".format(k))
                    removedPlayers.append(k)
                else:
                    # remove bet, total, and cards from players
                    for j in range(1, len(playerInfo[k])):
                        del playerInfo[k][1]
            removedPlayers.sort(reverse=True)
            for n in removedPlayers:
                del playerInfo[n]
            playerCount -= len(removedPlayers)
            if playerCount == 0:
                print("All players have gone bankrupt!\nBetter luck next time!")
                playing = False
            else:
                print("New Game")

        elif playMenu == "N":
            print("Thanks for playing!")
            playing = False


main()
