/************************************************************************
	Function Title: Programming Project 5
	Author: Jethro Carter Watson
	Summary: User enters the numbers 1-16 in any order, the numbers are
			 arranged into a 4X4 grid and the column, row, and diagnol
			 sums are displayed
************************************************************************
BEGIN
	TAKE INPUT FROM USER
	ARRANGED NUMBERS IN ARRAY
	ADD COLUMNS
	ADD ROWS
	ADD DIAGNOLS
	PRINT COLUMN SUMS
	PRINT ROW SUMS
	PRINT DIAGNOL SUMS
END
*************************************************************************/

#include <stdio.h>

int main()
{
	//initialize variables
	int x1, x2, x3, x4, x5, x6, x7, x8,
		x9, x10, x11, x12, x13, x14, x15, x16;
	int col1, col2, col3, col4;
	int row1, row2, row3, row4;
	int diagnol1, diagnol2;

	//Take input from user
	printf("Enter every number from 1 to 16 including 1 & 16 \n");
	scanf_s("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",
		&x1, &x2, &x3, &x4, &x5, &x6, &x7, &x8,
		&x9, &x10, &x11, &x12, &x13, &x14, &x15, &x16);

	//add rows
	row1 = x1 + x2 + x3 + x4;
	row2 = x5 + x6 + x7 + x8;
	row3 = x9 + x10 + x11 + x12;
	row4 = x13 + x14 + x15 + x16;

	//add columns
	col1 = x1 + x5 + x9 + x13;
	col2 = x2 + x6 + x10 + x14;
	col3 = x3 + x7 + x11 + x15;
	col4 = x4 + x8 + x12 + x16;

	//add diagnols
	diagnol1 = x1 + x6 + x11 + x16;
	diagnol2 = x4 + x7 + x10 + x13;

	printf("%d %d %d %d \n", x1, x2, x3, x4);
	printf("%d %d %d %d \n", x5, x6, x7, x8);
	printf("%d %d %d %d \n", x9, x10, x11, x12);
	printf("%d %d %d %d \n", x13, x14, x15, x16);

	//Print row sums
	printf("Row Sums: %d %d %d %d \n", row1, row2, row3, row4);
	//Print column sums
	printf("Column Sums: %d %d %d %d \n", col1, col2, col3, col4);
	//Print diagnol sums
	printf("Diagnol Sums: %d %d \n", diagnol1, diagnol2);

	return 0;

}
