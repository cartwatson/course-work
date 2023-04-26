#include "gtest.h"

#include "ComplexCalculator.hpp"

TEST(Complex, Add)
{
  ComplexCalculator calc;
  calc.run("5.1+3.6i + 34.1+4.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("39.2 + 7.7i", result);
}

TEST(Complex, AddNegatives1)
{
  ComplexCalculator calc;
  calc.run("-5.1+3.6i + 34.1-4.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("29.0 - 0.5i", result);
}

TEST(Complex, AddNegatives2)
{
  ComplexCalculator calc;
  calc.run("-5.1-3.6i + 2.1+4.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("-3.0 + 0.5i", result);
}

TEST(Complex, Subtract)
{
  ComplexCalculator calc;
  calc.run("5.6+7.6i - 4.2+4.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("1.4 + 3.5i", result);
}

TEST(Complex, SubtractNegatives)
{
  ComplexCalculator calc;
  calc.run("5.6-7.6i - -4.2+4.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("9.8 - 11.7i", result);
}

TEST(Complex, Multiplication)
{
  ComplexCalculator calc;
  calc.run("1.0-3.0i * 2.0+5.0i");
  std::string result = calc.getResult();

  EXPECT_EQ("17.0 - 1.0i", result);
}

TEST(Complex, MultiplicationNegatives)
{
  ComplexCalculator calc;
  calc.run("4.7-3.4i * -2.9+5.1i");
  std::string result = calc.getResult();

  EXPECT_EQ("3.7 + 33.8i", result);
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  return RUN_ALL_TESTS();
}
