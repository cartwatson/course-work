#ifndef BANK_HPP
#define BANK_HPP

#include <string>
#include "Account.hpp"

class Bank
{
    public:
        //constructors
        Bank();
        Bank(int numberOfAccounts);
        //public functions
        int getCount();
        void process(std::string line);
        //operator overloading
        Account*& operator[](int index)
        {
            return bank[index];
        }

    private:
        Account** bank;
        int numberOfAccounts;
        int accountCounter;
};

#endif //BANK_HPP