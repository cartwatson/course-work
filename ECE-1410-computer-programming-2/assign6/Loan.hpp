#ifndef LOAN_HPP
#define LOAN_HPP

#include <string>
#include "Account.hpp"

class Loan : public Account
{
    public:
        //constructors
        Loan();
        Loan(std::string name, float balance, float rate);
        //functions of Loan
        void transaction(float transAmount);
        void update();
    protected:
        //protected variables
        float rate;
};

#endif //LOAN_HPP