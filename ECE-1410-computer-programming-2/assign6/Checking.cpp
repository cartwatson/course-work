#include "Checking.hpp"

//----------------------------------------------------------------------------------
#include <iostream>

Checking::Checking()
{
    //empty
}

Checking::Checking(std::string name, float balance, float fee)
{
    //intialize variables
    this->name = name;
    this->balance = balance;
    this->fee = fee;
    //start fee counter
    numberOfTransactions = 0;
}

void Checking::transaction(float transAmount)
{
    //overdraft protection
    if ((transAmount + balance) < 0)
    {
        //account overdrawn
        balance -= 25;
        //message to user
        std::cout << "Account was overdrawn. $25 fine" << std::endl;
    } 
    else
    {
        //change balance
        balance += transAmount;
        //if check, charge fee
    }
    if (transAmount < 0) 
    {
        //add one to fee counter
        numberOfTransactions++;
    }
}

void Checking::update()
{
    //calc new balance
    balance -= numberOfTransactions * fee;
    //reset counter
    numberOfTransactions = 0;
}