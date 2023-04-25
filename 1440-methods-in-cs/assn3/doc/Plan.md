# 0.  From Problem Analysis to Data Definitions

**Program should display a menu that lets users create decks of bingo  
cards.  There will be limitations on the size of, and the quantity of  
the bingo cards.  The amount of bingo cards will range from 3-10000, the  
the maximum number in the card will be a function of the size of the  
bingo card.  Bingo cards can be both even and odd sizes; odd sized cards  
will have a free space in the very middle, even will not.**


# 1.  System Analysis

**Program uses an interactive menu to get data from the user.  This data  
is used to determine the bingo card size and quantity as well as the  
range for the number set it uses.  The menu is also used to instantiate  
or save the deck depending on the option selected by the user.  The  
option selected will be a single character for all options except saving  
which will require a file name.  Program will not take command line  
arguments.**

**Program gives output through the terminal. All output will be put in  
the terminal, saving the deck to a file being the only exception to  
this. All output is text however the bingo cards are formatted to appear  
as bingo cards. Output files from saving the deck will be .txt**

**The only formula will be used to determine the valid numbers for the  
numberSet, 2\*size\*size through 4\*size\*size.**

**The data each method and class used is in the UML diagram.**


# 2.  Functional Examples

**The menu will be the first point of interaction for users.  Options  
will be handled using the menuOption subclass. Program will wait for  
a valid menu option before proceeding. If an invalid option is a  
selected program will display a message telling the user they selected  
invalid input and will prompt for valid input.  When the user creates a  
deck the user will be prompted for valid numerical inputs.  In the case  
of invalid input program will continue to prompt user until valid input  
is selected.**


# 3.  Function Template

**Program runs, more implementation required for full functionality**


# 4.  Implementation

**Program runs according to plan and requirements.**

**Added _printOdd() and _printEven() methods to Card.py in order to handle different sized cards.**

**Added getters to Deck.py and NumberSet.py so as not to have to access a private variable in testing.**


# 5.  Testing

**To launch the program navigate to /cs1440-watson-jethro-assn3 in a shell.**

**To run the program input 'Python src/Bingo.py' in the shell and press enter**

**Input 'C' to create a deck, alternatively test exit function by inputting 'X'. If 'X' is input, relaunch the program.**

**To test the menu input any character that is not 'C' or 'X', program should ask for a menu selection again.**

**When 'C' is input in the main menu program will ask for parameters of a new deck.  To test program, input numbers outside the range given and then inside the range.  Program should ask for input again when invalid input is given.**

**After deck is created input any character that is not 'P', 'D', 'S', or 'X'.  Program should ask for input until valid input is given.**

**Input 'P' and then a number that is greater than the number of cards generated or less than one, program should go back to Deck menu.**

**Input 'P' again, input a valid number (1-# of cards created). Program should print readable bingo card.**

**Input 'D', program should display all cards to the terminal.**

**Input 'S', program should ask for a file name. Any input is accepted here. Verify that the program created and populated the new file.**

**Input 'X', program should exit to the main menu.**

**Functionality has been tested, alternately run 'Python runTests.py' to call the testSuite.**
