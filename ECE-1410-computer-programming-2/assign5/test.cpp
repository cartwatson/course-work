#include <iostream>
#include <sstream>

#include "gtest.h"

#include "Shape.hpp"
#include "Point.hpp"
#include "Circle.hpp"
#include "Cylinder.hpp"

std::streambuf* oldStdoutBuffer = NULL;
std::stringstream buffer;

std::ostream& operator<<(std::ostream &out, Shape &shape)
{
  out << shape.print();

  return out;
}

void grabStdout()
{
  oldStdoutBuffer = std::cout.rdbuf();
  std::cout.rdbuf(buffer.rdbuf());
}

void releaseStdout()
{
  buffer.str("");
  std::cout.rdbuf(oldStdoutBuffer);
}

TEST(Point, getX)
{
  Point p(4.0f, 5.0f);

  EXPECT_FLOAT_EQ(4.0f, p.getX());
}

TEST(Point, getY)
{
  Point p(4.0f, 5.0f);

  EXPECT_FLOAT_EQ(5.0f, p.getY());
}

TEST(Point, print)
{
  grabStdout();

  Point p(4.0f, 5.0f);
  std::cout << p;

  EXPECT_EQ("Point: [4.0,5.0]", buffer.str());

  releaseStdout();
}

TEST(Circle, getX)
{
  Circle c(12.2f, 23.8f, 1.6f);

  EXPECT_EQ(12.2f, c.getX());
}

TEST(Circle, getY)
{
  Circle c(12.2f, 23.8f, 1.6f);

  EXPECT_EQ(23.8f, c.getY());
}

TEST(Circle, getRadius)
{
  Circle c(12.2f, 23.8f, 1.6f);

  EXPECT_EQ(1.6f, c.getRadius());
}

TEST(Circle, getArea)
{
  Circle c(12.2f, 23.8f, 1.6f);

  EXPECT_FLOAT_EQ(8.04248f, c.getArea());
}

TEST(Circle, print)
{
  grabStdout();

  Circle c(12.2f, 23.8f, 1.6f);

  std::cout << c;

  EXPECT_EQ("Point: [12.2,23.8]; Circle: R(1.6), Area(8.04248)", buffer.str());

  releaseStdout();
}

TEST(Cylinder, getX)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_EQ(9.2f, c.getX());
}

TEST(Cylinder, getY)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_EQ(14.7f, c.getY());
}

TEST(Cylinder, getRadius)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_EQ(7.6f, c.getRadius());
}

TEST(Cylinder, getHeight)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_EQ(42.5f, c.getHeight());
}

TEST(Cylinder, getArea)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_FLOAT_EQ(2392.3855f, c.getArea());
}

TEST(Cylinder, getVolume)
{
  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  EXPECT_FLOAT_EQ(7711.98f, c.getVolume());
}

TEST(Cylinder, print)
{
  grabStdout();

  Cylinder c(9.2f, 14.7f, 7.6f, 42.5f);

  std::cout << c;

  EXPECT_EQ("Point: [9.2,14.7]; Circle: R(7.6), Area(181.458); Cylinder: H(42.5), Area(2392.39), Volume(7711.98)", buffer.str());

  releaseStdout();
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);

  return RUN_ALL_TESTS();
}
