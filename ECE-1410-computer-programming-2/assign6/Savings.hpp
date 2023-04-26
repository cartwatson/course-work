#ifndef SAVINGS_HPP
#define SAVINGS_HPP

#include <string>
#include "Account.hpp"

class Savings : public Account
{
    public:
        //constructors
        Savings();
        Savings(std::string name, float balance, float rate);
        //functions of Savings
        void transaction(float transAmount);
        void update();

    protected:
        //protected variables
        float rate;
};

#endif //SAVINGS_HPP
