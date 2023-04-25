import MenuOption


class Menu(): 
    def __init__(self, header):
        """Menu constructor"""
        self._header = header
        self._optionCount = 0
        self._options = []

    def addOption(self, command, description):
        """Add an option to the menu"""
        if command is not None and command != "":
            self._options.append(MenuOption.MenuOption(command, description))
            self._optionCount += 1

    def __isValidCommand(self, command):
        """Check that a command is contained in our list of menu options"""
        isValid = False
        if command == "X":
            isValid = True
        else:
            for i in range(self.getOptionCount()):
                if command == self.getOption(i).getCommand():
                    isValid = True
                    break
        return isValid

    def getOption(self, optionIndex):
        option = None
        if optionIndex >= 0 and optionIndex < self.getOptionCount():
            option = self._options[optionIndex]
        return option

    def getHeader(self):
        return self._header

    def getOptionCount(self):
        return self._optionCount

    def show(self):
        """Display the menu and take a command from the user"""
        command, keepGoing = '', True

        while keepGoing:
            optionList = ''

            print()
            print(self.getHeader(), "menu:")

            for i in range(self.getOptionCount()):
                option = self.getOption(i)
                if option is not None:
                    # 1st field is 6 chars wide
                    print(f"{option.getCommand()} - {option.getDescription()}")
                    optionList += option.getCommand() + ", "

            print("X - Exit")
            optionList += "X"

            print(f"\nEnter a {self.getHeader()} command ({optionList})")
            command = input()
            keepGoing = not self.__isValidCommand(command)

        return command
