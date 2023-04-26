#include <iostream>
#include <sstream>
#include "Bank.hpp"
#include "Savings.hpp"
#include "Checking.hpp"
#include "Loan.hpp"

//default constructor
Bank::Bank()
{
    bank = new Account*[1];
    this->numberOfAccounts = 1;
    accountCounter = 0;
}

//overloaded constructor
Bank::Bank(int numberOfAccounts)
{
    bank = new Account*[numberOfAccounts];
    this->numberOfAccounts = numberOfAccounts;
    accountCounter = 0;
}

//get count function
int Bank::getCount() 
{
    return accountCounter;
}

//Bank process function
void Bank::process(std::string line)
{
    //declare local variables
    char symbol;
    int accountNumber;
    std::string name;
    float balance;
    float rateFee;

    //put line into stringstream
    std::stringstream inputStream;
    inputStream << line;
    inputStream >> symbol;

    switch (symbol)
    {
        case 's': //savings
            //parse stream
            inputStream >> accountNumber >> name >> balance >> rateFee;
            //create savings
            bank[accountCounter] = new Savings(name, balance, rateFee);
            accountCounter++;
            break;

        case 'c': //checking
            //parse stream
            inputStream >> accountNumber >> name >> balance >> rateFee;
            //create checking
            bank[accountCounter] = new Checking(name, balance, rateFee);
            accountCounter++;
            break;

        case 'l': //create loan
            //parse stream
            inputStream >> accountNumber >> name >> balance >> rateFee;
            //create loan
            bank[accountCounter] = new Loan(name, balance, rateFee);
            accountCounter++;
            break;

        case 't': //transaction
            //parse stream
            inputStream>> accountNumber>> balance;
            //call virtual transaction
            bank[accountNumber]->transaction(balance);
            break;

        case 'u': //update
            //parse stream
            inputStream >> accountNumber;
            //call virtual update
            bank[accountNumber]->update();
            break;

        default:
            //error
            break;
    }
}