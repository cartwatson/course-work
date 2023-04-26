#include "Point.hpp"

#include <sstream>
#include <iomanip>

using namespace std;

Point::Point()
{
    //empty
}

Point::Point(float valX, float valY)
{
    m_valX = valX;
    m_valY = valY;
}

float Point::getX()
{
    return m_valX;
}

float Point::getY()
{
    return m_valY;
}

string Point::print()
{
    stringstream a;
    
    //manipulate stream
    a << std::fixed << std::setprecision(1);
    a << "Point: [" << m_valX << "," << m_valY << "]";

    return a.str();
}