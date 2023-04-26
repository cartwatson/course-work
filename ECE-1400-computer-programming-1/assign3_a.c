/***************************************************************************************
	Function title: Program 7
	Author: Jethro Watson
	
	Inputs: User
	Outputs: Print to screen
	
	Summary: Program inputs 4 integers and the largest and smallest are printed out
	
	Compile Instructions: gcc program3_project7.c -o project7.exe

****************************************************************************************
									PSEUDOCODE
BEGIN
	INTIALIZE VARIABLES
	GET FOUR INTEGERS FROM USER
	DETERMINE LARGEST AND SMALLEST INTEGERS
		max and min of a&b
		max and min of c&d
		max of ab and cd
		min of ab and cd
	PRINT LARGEST AND SMALLEST INTEGERS
END
***************************************************************************************/
#include <stdio.h>

int main()
{

//intialize variables
int a, b, c, d;
int t1, t2, t3, t4;
int MAXab, MINab, MAXcd, MINcd, MAX, MIN;

//get four intergers from user
printf("Enter four integers (eg: w, x, y, z): ");
scanf("%d, %d, %d, %d", &a, &b, &c, &d);

//run some tests to make typing easier
t1 = a > b;
t2 = b > c;
t3 = c > d;
t4 = d > a;

//determine largest and smallest value value

//max and min of a&b
if (t1) {
	MAXab = a;
	MINab = b;
} else {
	MAXab = b;
	MINab = a;
}

//max and min of c&d
if (t3) {
	MAXcd = c;
	MINcd = d;
} else {
	MAXcd = d;
	MINcd = c;
}

//max of ab and cd
if (MAXab > MAXcd) {
	MAX = MAXab;
} else {
	MAX = MAXcd;
}

//min of ab and cd
if (MINab < MINcd) {
	MIN = MINab;
} else {
	MIN = MINcd;
}

//print values of MAX and MIN
printf("Largest: %d\n", MAX);
printf("Smallest: %d\n", MIN);

return 0;
}