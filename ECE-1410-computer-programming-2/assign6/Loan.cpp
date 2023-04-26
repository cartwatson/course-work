#include "Loan.hpp"

Loan::Loan()
{
    //empty
}

Loan::Loan(std::string name, float balance, float rate)
{
    //intialize variables
    this->name = name;
    this->balance = balance;
    this->rate = rate;
}

void Loan::transaction(float transAmount)
{
    //adjust balance
    balance -= transAmount;
}

void Loan::update()
{
    //add interest to balance
    balance += balance * rate;
}