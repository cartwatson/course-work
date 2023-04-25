# import class Password
from password import Password


def main():
    # initialize while loop
    done = False

    while not done:
        # create object
        password = Password()

        # get possible password
        message = input("Enter a possible password: ")

        # pass possible password to object
        password.setPassword(message)

        # if password is valid print tell user
        if password.isValid():
            print("Password is valid")
        # else print error message
        else:
            print(password.getErrorMessage())

        # initialize again
        again = ""

        # ask user if they want to try another password
        while again != "Y" or "N":
            again = input("Would you like to try another password (Y/N): ").upper()
            if again == "N":  # user said no, terminate program
                done = True
                print("Thanks for validating your password(s)!")
                print("Now terminating program...")
                break
            elif again == "Y":  # user said yes, keep running
                done = False
                break
            else:  # user inputted wrong str try again
                while again != "Y" or "N":
                    again = input("Would you like to try another password (Y/N): ").upper()
                    if again == "N":  # user said no, terminate program
                        done = True
                        print("Thanks for validating your password(s)!")
                        print("Now terminating program...")
                        break
                    elif again == "Y":  # user said yes, keep running
                        done = False
                        break  # exit first while
                break  # exit second while


main()
