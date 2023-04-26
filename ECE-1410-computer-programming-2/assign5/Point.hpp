#ifndef POINT_HPP
#define POINT_HPP

#include "Shape.hpp"

#include <iostream>
#include <sstream>

class Point : public Shape
{
    public:
        //constructor
        Point();
        Point(float m_valX, float m_valY); //overload
        //methods
        float getX();
        float getY();
        std::string print();


    protected:
        //protected variables
        float m_valX;
        float m_valY;

    private:

};

#endif //POINT_HPP
