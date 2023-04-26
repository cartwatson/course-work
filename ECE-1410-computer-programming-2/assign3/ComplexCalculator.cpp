#include "ComplexCalculator.hpp"

#include <string>
#include <sstream>
#include <math.h>
#include <iomanip>

using namespace std;

//complex class
Complex::Complex() 
{
    //empty
}

string Complex::toString()
{
    stringstream output;
    char middle;
    if (imaginary < 0) 
    {
        middle = '-';
        this->setImaginary(fabs(this->getImaginary()));
    } else {
        middle = '+';
    }

    output << std::fixed << std::setprecision(1);
    output << this->getReal() << " " << middle << " " << this->getImaginary() << "i";
    return output.str(); 
}

Complex Complex::add(Complex other) 
{
    float real = this->getReal() + other.getReal();
    float imaginary = this->getImaginary() + other.getImaginary();
    Complex newComplex;
    newComplex.setReal(real);
    newComplex.setImaginary(imaginary);
    return newComplex;
}

Complex Complex::subtract(Complex other) 
{
    float real = this->getReal() - other.getReal();
    float imaginary = this->getImaginary() - other.getImaginary();
    Complex newComplex;
    newComplex.setReal(real);
    newComplex.setImaginary(imaginary);
    return newComplex;
}

Complex Complex::multiply(Complex other)
{
    float real = this->getReal() * other.getReal() + this->getImaginary() * other.getImaginary() * -1.0;
    float imaginary = this->getReal() * other.getImaginary() + this->getImaginary() * other.getReal();
    Complex newComplex;
    newComplex.setReal(real);
    newComplex.setImaginary(imaginary);
    return newComplex;
}

//complex calc class
ComplexCalculator::ComplexCalculator() 
{
    //empty
}
void ComplexCalculator::run(std::string equation)
{
    //declare variables
    char trash1;
    char trash2;
    float real1;
    float imaginary1;
    float real2;
    float imaginary2;
    char operationL;
 
    //string streams
    stringstream newIn;
    newIn << equation;

    newIn >> real1 >> imaginary1 >> trash1 >> operationL >> real2 >> imaginary2 >> trash2;

    this->setA(real1, imaginary1);
    this->setOperation(operationL);
    this->setB(real2, imaginary2);
}

string ComplexCalculator::getResult(void)
{
    Complex output;
    switch (this->getOperation())
    {
        case '+':
            output = (this->getA()).add((this->getB()));
            return output.toString();
        case '-':
            output = (this->getA()).subtract((this->getB()));
            return output.toString();
        case '*':
            output = (this->getA()).multiply((this->getB()));
            return output.toString();
        default:
            //invalid operation 
            break;
    }
}