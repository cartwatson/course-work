#include <iostream>
#include <string>
#include <sstream>

#include "gtest.h"

#include "Complex.hpp"

std::streambuf* oldCin;
std::streambuf* oldCout;

std::stringstream newCin;
std::stringstream newCout;

class Ece1410Environment : public ::testing::Environment
{
public:
  ~Ece1410Environment() override {}

  // Override this to define how to set up the environment.
  void SetUp() override
  {
    oldCin = std::cin.rdbuf();
    std::cin.rdbuf(newCin.rdbuf());

    oldCout = std::cin.rdbuf();
    std::cout.rdbuf(newCout.rdbuf());
  }

  // Override this to define how to tear down the environment.
  void TearDown() override
  {
    std::cin.rdbuf(oldCin);
    std::cout.rdbuf(oldCout);
  }
};

TEST(Complex, bothPositive)
{
  Complex myComplex;

  newCin << "3.14+2.54i\n";

  myComplex.readInput();

  EXPECT_EQ(newCout.str(), "Input a complex number: ");
  newCout.str("");

  myComplex.printOutput();

  EXPECT_EQ(newCout.str(), "Real: 3.14\nImaginary: 2.54\n");
  newCout.str("");
}

TEST(Complex, negativeReal)
{
  Complex myComplex;

  newCin << "-3.14+2.54i\n";

  myComplex.readInput();

  EXPECT_EQ(newCout.str(), "Input a complex number: ");
  newCout.str("");

  myComplex.printOutput();

  EXPECT_EQ(newCout.str(), "Real: -3.14\nImaginary: 2.54\n");
  newCout.str("");
}

TEST(Complex, negativeImaginary)
{
  Complex myComplex;

  newCin << "3.14-2.54i\n";

  myComplex.readInput();

  EXPECT_EQ(newCout.str(), "Input a complex number: ");
  newCout.str("");

  myComplex.printOutput();

  EXPECT_EQ(newCout.str(), "Real: 3.14\nImaginary: -2.54\n");
  newCout.str("");
}

TEST(Complex, bothNegative)
{
  Complex myComplex;

  newCin << "-3.14-2.54i\n";

  myComplex.readInput();

  EXPECT_EQ(newCout.str(), "Input a complex number: ");
  newCout.str("");

  myComplex.printOutput();

  EXPECT_EQ(newCout.str(), "Real: -3.14\nImaginary: -2.54\n");
  newCout.str("");
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  ::testing::Environment *const foo_env = ::testing::AddGlobalTestEnvironment(new Ece1410Environment);

  return RUN_ALL_TESTS();
}