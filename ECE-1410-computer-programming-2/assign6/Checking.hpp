#ifndef CHECKING_HPP
#define CHECKING_HPP

#include <string>
#include "Account.hpp"

class Checking : public Account
{
    public:
        //constructors
        Checking();
        Checking(std::string name, float balance, float fee);
        //functions of checking
        void transaction(float transAmount);
        void update();

    protected:
        //protected variables
        float fee;
        float numberOfTransactions;
};

#endif //CHECKING_HPP