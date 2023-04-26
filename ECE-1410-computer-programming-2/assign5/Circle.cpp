#include "Circle.hpp"
#include "Point.hpp"
#include "Shape.hpp"

#include <sstream>

Circle::Circle()
{
    //empty
}

Circle::Circle(float valX, float valY, float radius)
{
    m_valX = valX;
    m_valY = valY;
    m_radius = radius;
}

float Circle::getRadius()
{
    return m_radius;
}

float Circle::getArea()
{
    float area = 3.14159265358979323846 * m_radius * m_radius;

    return area;
}

std::string Circle::print()
{
    Point p(m_valX, m_valY);

    std::stringstream a;

    a << p.print() << "; Circle: R(" << this->getRadius() << "), Area(" << this->getArea() << ")";

    return a.str();
}