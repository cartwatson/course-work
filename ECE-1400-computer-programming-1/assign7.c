/******************************************************************
	Program Title: polynomial checker
	Author: Jethro C Watson

	Inputs: user inputs value of x
	Outputs: result of computation

	Summary: user value of x is plugged into polynomial result
			 is returned

******************************************************************
BEGIN
	INTIALIZE VARIABLES
	SHOW USER POLYNOMIAL
	GET VALUE OF X FROM USER
	CALL FUNCTION
		INPUT VALUE OF X INTO POLYNOMIAL
		COMPUTE
		RETURN COMPUTATION
	PRINT RESULT
END
******************************************************************/

#include <stdio.h>

float polynomial(float x);

int main()
{
	//intialize variables
	float x;

	//show polynomial to user
	printf("The polynomial is... \n 3x^5 + 2x^4 - 5x^3 - x^2 + 7x - 6 \n");
	//get value from user
	printf("Enter the value of x: ");
	scanf_s("%f", &x);

	//call function to compute polynomial
	//print result
	printf("The value of the function is: ");
	printf("%f", polynomial(x));
}

float polynomial(float x) {
	//intilize local variables
	float result;

	//calculate value of polynomial
	result = 3 * x * x * x * x * x;
	result += 2 * x * x * x * x;
	result -= 5 * x * x * x;
	result -= x * x;
	result += 7 * x;
	result -= 6;

	return result;

}
