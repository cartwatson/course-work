#include "Savings.hpp"
#include <iostream>

Savings::Savings()
{
    //empty
}

Savings::Savings(std::string name, float balance, float rate)
{
    //intialize variables
    this->name = name;
    this->balance = balance;
    this->rate = rate; 
}

void Savings::transaction(float transAmount)
{
    //overdraft protection
    if ((transAmount + balance) < 0)
    {
        //overdrawn
        //message to user
        std::cout << "Account was overdrawn" << std::endl;
    } 
    else
    {
        //add transaction amount to balance
        balance += transAmount;
    }
}

void Savings::update()
{
    //calculate interest and add it
   balance += balance * rate; 
}