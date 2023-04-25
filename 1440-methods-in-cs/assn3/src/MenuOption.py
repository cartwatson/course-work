class MenuOption():
    def __init__(self, command, description):
        self._command = command
        self._description = description

    def getCommand(self):
        return self._command

    def getDescription(self):
        return self._description

