#include <time.h>
#include <cstdlib>

#include "gtest.h"
#include "Sorts.hpp"

#define SMALL 10
#define BIG 10000

class Environment : public ::testing::Environment {
 public:
  virtual ~Environment() {}

  void SetUp() override
  {
    srand(time(NULL));
  }  
};

int* generateRandomArray(int length)
{

  int* pArray = new int[length];

  for (int i = 0; i < length; ++i)
  {
    pArray[i] = rand() % length;
  }

  return pArray;
}

void printArray(int* pArray, int length)
{
  for (int i = 0; i < length; ++i)
  {
    std::cout << pArray[i] << " ";
  }

  std::cout << std::endl;
}

void checkArray(int* pArray, int length)
{
  for (int i = 0; i < length - 1; ++i)
  {
    ASSERT_LE(pArray[i], pArray[i + 1]);
  }
}

TEST(SmallSort, Bubble)
{
  int* pArray = generateRandomArray(SMALL);

  printArray(pArray, SMALL);
  
  Sorts sorter;

  sorter.bubble(pArray, SMALL);

  printArray(pArray, SMALL);
  checkArray(pArray, SMALL);
}

TEST(BigSort, Bubble)
{
  int* pArray = generateRandomArray(BIG);

  Sorts sorter;

  sorter.bubble(pArray, BIG);

  checkArray(pArray, BIG);
}

TEST(SmallSort, Selection)
{
  int* pArray = generateRandomArray(SMALL);

  printArray(pArray, SMALL);
  
  Sorts sorter;

  sorter.selection(pArray, SMALL);

  printArray(pArray, SMALL);
  checkArray(pArray, SMALL);
}

TEST(BigSort, Selection)
{
  int* pArray = generateRandomArray(BIG);

  Sorts sorter;

  sorter.selection(pArray, BIG);

  checkArray(pArray, BIG);
}

TEST(SmallSort, Quick)
{
  int* pArray = generateRandomArray(SMALL);

  printArray(pArray, SMALL);
  
  Sorts sorter;

  sorter.quick(pArray, SMALL);

  printArray(pArray, SMALL);
  checkArray(pArray, SMALL);
}

TEST(BigSort, Quick)
{
  int* pArray = generateRandomArray(BIG);

  Sorts sorter;

  sorter.quick(pArray, BIG);

  checkArray(pArray, BIG);
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  ::testing::AddGlobalTestEnvironment(new Environment);

  return RUN_ALL_TESTS();
}