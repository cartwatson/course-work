/******************************************************************
	Program Title: UPC Code checker
	Author: Jethro C Watson

	Inputs: user inputs digits of UPC
	Outputs: check digit for UPC

	Summary: user inputs 12 digits of European UPC, Program
			 calculates check digit

******************************************************************
BEGIN
	ASK USER FOR FIRST 12 DIGITS OF UPC
	ADD SECOND, FOURTH, SIXTH, EIGHTH, TENTH, AND TWELFTH DIGITS
	ADD FIRST, THRID, FIFTH, SEVENTH, NINTH, AND ELEVENTH DIGITS
	MULTIPLY THE FIRST SUM BY 3 AND ADD IT TO THE SECOND SUM
	SUBTRACT 1 FROM THE TOTAL
	COMPUTE THE REMAINDER WHEN THE ADJUSTED TOTAL IS DIVIDED BY 10
	SUBTRACT THE REMAINDER FROM 9
	PRINT CHECK DIGIT
END
******************************************************************/

#include <stdio.h>

int main(void)
{
	//intialize variables
	int d, i1, i2, i3, i4, i5, i6, j1, j2, j3, j4, j5,
		first_sum, second_sum, total;

	//ask user for first 12 digits of UPC
	printf("Enter all tweleve digits: ");
	scanf_s("%1d %1d %1d %1d %1d %1d %1d %1d %1d %1d %1d %1d",
		&d, &i1, &i2, &i3, &i4, &i5, &i6,
		&j1, &j2, &j3, &j4, &j5);

	//add the second, fourth, sixth, eighth, tenth, and twevelth digits
	first_sum = i1 + i3 + i5 + j1 + j3 + j5;
	second_sum = d + i2 + i4 + i6 + j2 + j4;

	//mulitiply the first sum by 3 and add it to the second sum
	total = (3 * first_sum) + second_sum;

	//subtract 1 from total, calculate remainder when divided by 10
	//subtract remainder from 9
	total = 9 - ((total - 1) % 10);

	//print check digit
	printf("Check digit: %d\n", total);

	return 0;
}