/******************************************************************
	Program Title: Newtonian square root calculator
	Author: Jethro C Watson

	Inputs: user inputs positive number
	Outputs: displays square root

	Summary: calculates square root of positive number via 
			 newtonian method.

******************************************************************
BEGIN
	INCLUDE STDIO.H AND MATH.H
	INTIALIZE VARIABLES
	ASK USER FOR A POSITIVE NUMBER
	START CALCULATION USING FOR LOOP
	DISPLAY SQUARE ROOT
END
******************************************************************/

//include necessary libraries
#include <stdio.h>
#include <math.h>

int main()
{
	//itialize variables
	double x, y1, y2, d, a;
	
	//ask user for positive number
	printf("Enter a positive number: ");
	scanf("%lf", &x);
			
	//start calculation
	for(y1 = 1, y2  = 0; fabs(y1 - y2) > 0.00001 * y1;)
	{
		d = x / y1;
		a = (d + y1) / 2.0;
		y2 = y1;
		y1 = a;
		//print statements used in development to check results
		//printf("x/y: %lf \n", d);
		//printf("Ave of y & x/y: %lf \n", a);
		//printf("y2: %lf \n", y2);
		//printf("y1: %lf \n", y1);
	}

	//display square root
	printf("Square root: %.10lf \n", a);

	return 0;
}