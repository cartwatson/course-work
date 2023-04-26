#ifndef HELLO_HPP
#define HELLO_HPP

#include <string>

using namespace std;

class Hello
{
    public:
        string name;
        string getName()
        {
            return "Hello " + name;
        }  
};

#endif