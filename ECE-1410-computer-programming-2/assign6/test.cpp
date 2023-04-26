#include <iostream>
#include <fstream>
#include "gtest.h"

#include "Bank.hpp"

TEST(Bank, All)
{
  std::ifstream fin("bankAll.txt");
  std::string line;

  Bank bank;

  while(getline(fin, line))
  {
    bank.process(line);
  }

  EXPECT_EQ(3, bank.getCount());

  EXPECT_EQ("Dessie", bank[0]->getName());
  EXPECT_FLOAT_EQ(6622.875f, bank[0]->getBalance());
  
  EXPECT_EQ("Andrew", bank[1]->getName());
  EXPECT_FLOAT_EQ(15.75, bank[1]->getBalance());

  EXPECT_EQ("Hannah", bank[2]->getName());
  EXPECT_FLOAT_EQ(369.60, bank[2]->getBalance());
}

TEST(Bank, Savings)
{
  std::ifstream fin("bankSavings.txt");
  std::string line;

  Bank bank;

  while(getline(fin, line))
  {
    bank.process(line);
  }

  EXPECT_EQ(4, bank.getCount());

  EXPECT_EQ("Dessie", bank[0]->getName());
  EXPECT_FLOAT_EQ(174.21243, bank[0]->getBalance());
  
  EXPECT_EQ("Andrew", bank[1]->getName());
  EXPECT_FLOAT_EQ(1251.2207, bank[1]->getBalance());

  EXPECT_EQ("Hannah", bank[2]->getName());
  EXPECT_FLOAT_EQ(1164.625, bank[2]->getBalance());

  EXPECT_EQ("April", bank[3]->getName());
  EXPECT_FLOAT_EQ(3138.4285, bank[3]->getBalance());
}

TEST(Bank, Loan)
{
  std::ifstream fin("bankLoan.txt");
  std::string line;

  Bank bank;

  while(getline(fin, line))
  {
    bank.process(line);
  }

  EXPECT_EQ(1, bank.getCount());

  EXPECT_EQ("Melinda", bank[0]->getName());
  EXPECT_FLOAT_EQ(0.0, bank[0]->getBalance());
}

TEST(Bank, Checking)
{
  std::ifstream fin("bankChecking.txt");
  std::string line;

  Bank bank;

  while(getline(fin, line))
  {
    bank.process(line);
  }

  EXPECT_EQ(1, bank.getCount());

  EXPECT_EQ("Jacob", bank[0]->getName());
  EXPECT_FLOAT_EQ(1819811.00, bank[0]->getBalance());
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  return RUN_ALL_TESTS();
}