#ifndef CYLINDER_HPP
#define CYLINDER_HPP

#include "Shape.hpp"
#include "Point.hpp"
#include "Circle.hpp"
#include "Cylinder.hpp"

class Cylinder : public Circle
{
    public:
        //Constructer
        Cylinder();
        Cylinder(float valX, float valY, float radius, float height); //overload
        //methods
        float getHeight();
        float getArea();
        float getVolume();
        std::string print();

    protected:
        //protected cylinder variable
        float m_height;
        
    private:

};

#endif //CYLINDER_HPP
