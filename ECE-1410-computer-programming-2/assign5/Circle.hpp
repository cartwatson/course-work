#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include "Shape.hpp"
#include "Point.hpp"

class Circle : public Point
{
    public:
        //constructor
        Circle();
        Circle(float valX, float valY, float radius); //overload
        //member functions
        float getRadius();
        virtual float getArea();
        std::string print();

    protected:
        //protected circle variable
        float m_radius;

    private:
        
};

#endif //CIRCLE_HPP
