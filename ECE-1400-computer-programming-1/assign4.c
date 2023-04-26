/***************************************************************************************
	Function title: Program 11
	Author: Jethro Watson
	
	Inputs: User
	Outputs: Print to screen
	
	Summary: Calculates and prints value of e given a degree of accuracy
	
	Compile Instructions: gcc program4_project11.c -o project11.exe

****************************************************************************************
									PSEUDOCODE
BEGIN
	INTIALIZE VARIABLES
	GET DEGREE OF ACCURACY FROM USER
	USE LOOP TO CALCULATE e
	PRINT VALUE OF e
END
***************************************************************************************/

#include <stdio.h>

int main ()
{

//intialize variables	
int i, n;
float inc;
float e = 1;
unsigned long long fact = 1;

//get input from user
printf("Input degree of accuracy for calculating e: ");
scanf("%d", &n);

//use loop to calculate e to provided accuracy
	for(i = 1; i <= n; ++i)
	{
		fact *= i;
		inc = 1.0 / fact;
		e += inc;
	}

//print value of e
printf("The value of e is: %21.20f", e);

return 0;
}