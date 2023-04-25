from account import Account


def main():
    # get account id
    id = -1
    while id < 0:
        id = eval(input("Enter account ID: "))
        if id < 0:
            print("Please enter valid ID.")
            id = eval(input("Enter account ID: "))

    # get account balance
    balance = -1
    while balance < 0:
        balance = eval(input("Enter account balance: $"))
        if balance < 0:
            print("Please enter valid balance.")
            balance = eval(input("Enter account balance: $"))

    # get annualInterestRate
    annualInterestRate = -1
    while annualInterestRate < 0 or annualInterestRate > 10:
        annualInterestRate = eval(input("Enter annual interest rate: "))
        if annualInterestRate < 0 or annualInterestRate > 10:
            print("Please enter valid annual interest rate.")
            annualInterestRate = eval(input("Enter annual interest rate: "))

    # create object
    account = Account(id, balance, annualInterestRate)

    # initialize variable for while loop
    done = False

    while not done:
        # display menu
        print("(1) Display ID")
        print("(2) Display Balance")
        print("(3) Display Annual Interest Rate")
        print("(4) Display Monthly Interest Rate")
        print("(5) Display Monthly Interest")
        print("(6) Withdraw Money")
        print("(7) Deposit Money")
        print("(8) Exit")

        # user decision
        menu = eval(input())

        # what to display based on user decision
        if menu == 1:
            # display ID
            print("Account ID:", account.get_id())
        elif menu == 2:
            # display balance
            print("Balance: ${:.2f}".format(account.get_balance()))
        elif menu == 3:
            # display annual interest rate
            print("Annual Interest Rate: {:.2f}%".format(account.get_annualInterestRate()))
        elif menu == 4:
            # display monthly interest rate
            print("Monthly Interest Rate: {:.2f}%".format(account.get_monthlyInterestRate()))
        elif menu == 5:
            # display monthly interest
            print("Monthly Interest: ${:.2f}".format(account.get_monthlyInterest()))
        elif menu == 6:
            # withdraw inputted amount
            print("Current Balance: ${:.2f}".format(account.get_balance()))
            amount = -1
            while amount < 0:
                amount = eval(input("Enter amount to withdraw: $"))
                if amount < 0:
                    print("Please enter positive amount.")
                    amount = eval(input("Enter amount to withdraw: $"))
                    if account.get_balance() < amount:
                        print("Account will be overdrawn. Transaction not complete.")
                        overdrawn = True
                        break
                if account.get_balance() < amount and not overdrawn:
                    print("Account will be overdrawn. Transaction not complete.")
                else:
                    account.withdraw(amount)
                    print("Your new balance is: ${:.2f}".format(account.get_balance()))
        elif menu == 7:
            # deposit inputted amount
            print("Current Balance: ${:.2f}".format(account.get_balance()))
            amount = -1
            while amount < 0:
                amount = eval(input("Enter amount to deposit: $"))
                if amount < 0:
                    print("Please enter positive amount.")
                    amount = eval(input("Enter amount to deposit: $"))
            account.deposit(amount)
            print("Your new balance is: ${:.2f}".format(account.get_balance()))
        elif menu == 8:
            # exit while loop
            done = True
            print("Now exiting account...")
            print("Thanks for banking with CS 1400!")
        else:
            # invalid option chosen loop menu
            print("Please enter valid option.")


main()
