#ifndef COMPLEX_HPP
#define COMPLEX_HPP

#include <iostream>
#include <string>

using namespace std;

class Complex
{
  public:
    Complex() {}

    void readInput(void) {
      cout << "Input a complex number: ";
      cin >> real >> imaginary >> trash;
    }

    void printOutput(void) {
      cout << "Real: " << real << "\n" << "Imaginary: " << imaginary << endl;
    }

  private:
    char trash;
    float real;
    float imaginary;
};

#endif // COMPLEX_HPP
