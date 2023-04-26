/*********************************************************************************************
	Program Title: Break down into bills
	Author: Jethro C Watson

	Inputs: user inputs dollar amount
	Outputs: displays smallest number of $20 bills, $10 bills, 
			 $5 bills, and $1 bills

	Summary: calculates the smallest number of $20 bills, 
			 $10 bills, $5 bills, and $1 bills needed to break 
			 down the user inputted number and displays the 
			 number of bills.

*********************************************************************************************
BEGIN
	INCLUDE STDIO.H
	INTIALIZE pay_amount() FUNCTION
	CALL main() FUNCTION
		INTIALIZE VARIABLES
		ASK USER FOR A POSITIVE DOLLAR AMOUNT
		CALL pay_amount()
			INTIALIZE LOCAL VARIABLES
			CALCULATE NUMBER OF TWENTIES
			PRINT NUMBER OF TWENTIES
			CALCULATE NUMBER OF TENS
			PRINT NUMBER OF TENS
			CALCULATE NUMBER OF FIVES
			PRINT NUMBER OF FIVES
			PRINT NUMBER OF ONES
			DISPLAY RESULTS
END
*********************************************************************************************/

//include necessary libraries
#include <stdio.h>

//intialize pay amount function
void pay_amount(int dollars, int *twenties, int *tens, int *fives, int *ones);

int main() 
{
	//intialize variables
	int dollars;
	//intialize pointers
	int *twenties, *tens, *fives, *ones;
	
	//get input from user
	printf("Enter a whole dollar amount: ");
	scanf("%d", &dollars);

	//call pay_amount function
	pay_amount(dollars, twenties, tens, fives, ones);
}


void pay_amount(int dollars, int *twenties, int *tens, int *fives, int *ones) 
	{
		//int local variables
		int d20, d10, d05, d01;
		
		//calculate number of twenties
		twenties = &d20;
		d20 = dollars / 20;
		dollars %= 20;
		//print number of twenties
		printf("%11s %2d \n", "$20 Bills: ", *twenties);
		
		//calculate number of tens
		tens = &d10;
		d10 = dollars / 10;
		dollars %= 10;
		//print number of tens
		printf("%11s %2d \n", "$10 Bills: ", *tens);
		
		//calculate number of fives
		fives = &d05;
		d05 = dollars / 5;
		dollars %= 5;
		//print number of fives
		printf("%11s %2d \n", "$5 Bills: ", *fives);
		
		//calculate number of ones
		//what remains is the number of ones
		ones = &d01;
		d01 = dollars;
		//print number of ones
		printf("%11s %2d \n", "$1 Bills: ", *ones);	
	}