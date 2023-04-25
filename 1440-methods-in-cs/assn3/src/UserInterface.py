import Menu
from Deck import Deck


class UserInterface():
    def __init__(self):
        self._currentDeck = None
        pass

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        """Command to create a new Deck"""
        # validate all input as integers
        # card size is 3-15
        validInput = False
        while not validInput:
            size = input("Input card size: [3-15]\n")
            # check for digits
            if size.isnumeric():
                size = int(size)
                # check contents for size restraints
                if 3 <= size <= 15:
                    validInput = True
        # max num is range of 2*size*size and 4*size*size
        # compute max and min
        maxNum = 4*size*size
        minNum = 2*size*size
        validInput = False
        while not validInput:
            maxSize = input("Input max card number: [{min}-{max}]\n".format(min=minNum, max=maxNum))
            # check for digits
            if maxSize.isnumeric():
                maxSize = int(maxSize)
                # check contents for size restraints
                if minNum <= maxSize <= maxNum:
                    validInput = True
        # num of cards is 3-10000
        validInput = False
        while not validInput:
            numCards = input("Input number of cards: [3-10000]\n")
            # check for digits
            if numCards.isnumeric():
                numCards = int(numCards)
                # check contents for size restraints
                if 3 <= numCards <= 10000:
                    validInput = True
        # Create a new deck
        self._currentDeck = Deck(size, numCards, maxSize)
        # Display a deck menu and allow user to do things with the deck
        self.__deckMenu()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                self._currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print\n", 1, self._currentDeck.getCardCount())
        if cardToPrint > 0:
            self._currentDeck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name\n")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self._currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")

    def __getNumberInput(self, prompt, integer, cardCount):
        """get number input, return number"""
        while not False:
            num = input(prompt)
            # check for digits
            if num.isnumeric():
                return int(num)

    def __getStringInput(self, prompt):
        """get string input, return string"""
        # TODO: validate this
        string = input(prompt)
        return string