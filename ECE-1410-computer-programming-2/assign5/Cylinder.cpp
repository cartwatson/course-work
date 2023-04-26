#include "Shape.hpp"
#include "Point.hpp"
#include "Circle.hpp"
#include "Cylinder.hpp"

using namespace std;

Cylinder::Cylinder()
{
    //empty
}

Cylinder::Cylinder(float valX, float valY, float radius, float height)
{
    m_valX = valX;
    m_valY = valY;
    m_radius = radius;
    m_height = height;
}

float Cylinder::getHeight()
{
    return m_height;
}

float Cylinder::getArea()
{
    return 2 * 3.14159265358979323846 * m_radius * m_height + 2 * 3.14159265358979323846 * m_radius * m_radius;
}

float Cylinder::getVolume()
{
    return 3.14159265358979323846 * m_radius * m_radius * m_height;
}

std::string Cylinder::print()
{
    Circle c(m_valX, m_valY, m_radius);

    std::stringstream a;

    // Cylinder: H(42.5), Area(2392.39), Volume(7711.98)
    a << c.print() << "; Cylinder: H(" << this->getHeight() << "), Area(" << this->getArea() << "), Volume(" << this->getVolume() << ")";

    return a.str();
}