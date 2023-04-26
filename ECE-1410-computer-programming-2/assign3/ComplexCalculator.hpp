#ifndef COMPLEX_CALCULATOR_HPP
#define COMPLEX_CALCULATOR_HPP

#include <sstream>

using namespace std;

class Complex
{
    public:
      Complex();
      Complex(float real, float imaginary);
      std::string toString();
      Complex add (Complex other);
      Complex subtract (Complex other);
      Complex multiply (Complex other);

      //Private variable manipulators
      //setters
      void setReal(float a) {
        real = a;
      }
      void setImaginary(float a) {
        imaginary = a;
      }
      //getters
      float getImaginary(void) {
        return imaginary;
      }
      float getReal(void) {
        return real;
      }

    private:
      float real;
      float imaginary;
};

class ComplexCalculator
{
  public:
    ComplexCalculator();
    void run(std::string equation);
    std::string getResult(void);

    //Private variable manipulators
    //setters
    void setA(float real, float imaginary) {
      a.setReal(real);
      a.setImaginary(imaginary);
    }
    void setB(float real, float imaginary) {
      b.setReal(real);
      b.setImaginary(imaginary);
    }
    void setOperation(char i) {
      operation = i;
    }
    //getters
    Complex getA(void) {
      return a;
    }
    float getAreal(void) {
      return a.getReal();
    }
    float getAimaginary(void) {
      return a.getImaginary();
    }
    Complex getB(void) {
      return b;
    }
    float getBreal(void) {
      return b.getReal();
    }
    float getBimaginary(void) {
      return b.getImaginary();
    }
    char getOperation(void) {
      return operation;
    }

  private:
    Complex a;
    Complex b;
    char operation;
};

#endif // COMPLEX_CALCULATOR_HPP
