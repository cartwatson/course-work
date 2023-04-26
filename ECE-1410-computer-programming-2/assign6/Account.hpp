#ifndef ACCOUNT_HPP
#define ACCOUNT_HPP

#include <string>

class Account
{
    public:
        //constructor
        Account();
        //functions of account
        float getBalance();
        std::string getName();
        //virtual functions
        virtual void transaction(float transAmount);
        virtual void update();

    protected:
        //protected variables of account
        float balance;
        std::string name;
};

#endif //ACCOUNT_HPP
