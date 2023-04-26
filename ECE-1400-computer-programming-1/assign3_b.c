/***************************************************************************************
	Function title: Program 11
	Author: Jethro Watson
	
	Inputs: User
	Outputs: Print to screen
	
	Summary: Program prints phonetic pronunciation for a given two digit number
	
	Compile Instructions: gcc program3_project11.c -o project11.exe

****************************************************************************************
									PSEUDOCODE
BEGIN
	INTIALIZE VARIABLES
	GET TWO DIGIT NUMBER FROM USER
	DETERMINE PHONETIC PRONUNCIATION FOR FIRST DIGIT
	DETERMINE PHONETIC PRONUNCIATION FOR SECOND DIGIT
	PRINT PHONETIC PRONUNCIATION FOR FIRST DIGIT
	PRINT PHONETIC PRONUNCIATION FOR SECOND DIGIT
END
***************************************************************************************/
#include <stdio.h>

int main()
{

//intialize variables
int digit1, digit2;

//get two digit number from user
printf("Enter a two-digit number: ");
scanf("%1d", &digit1);
scanf("%1d", &digit2);

//test to make sure digit was recieved correctly
//printf("%d, %d\n", digit1, digit2);

//start print phrase
printf("You entered the number: ");

//determine phonetic pronunciation for first digit
switch (digit1) {
	case 1: switch (digit2) {
				case 1: printf("Eleven");
						digit2 = 0;
						break;
				case 2: printf("Twelve");
						digit2 = 0;
						break;
				case 3: printf("Thirteen");
						digit2 = 0;
						break;
				case 4: printf("Fourteen");
						digit2 = 0;
						break;
				case 5: printf("Fifteen");
						digit2 = 0;
						break;
				case 6: printf("Sixteen");
						digit2 = 0;
						break;
				case 7: printf("Seventeen");
						digit2 = 0;
						break;
				case 8: printf("Eighteen");
						digit2 = 0;
						break;
				case 9: printf("Nineteen");
						digit2 = 0;
						break;
			}
			break;
	case 2: printf("Twenty-");
			break;
	case 3: printf("Thirty-");
			break;
	case 4: printf("Forty-");
			break;
	case 5: printf("Fifty-");
			break;
	case 6: printf("Sixty-");
			break;
	case 7: printf("Seventy-");
			break;
	case 8: printf("Eighty-");
			break;
	case 9: printf("Ninety-");
			break;
}

//determine phonetic pronunciation for second digit

if (digit1 >= 20 || digit1 <= 10) { 
	switch (digit2) {
		case 1: printf("One");
			break;
		case 2: printf("Two");
			break;
		case 3: printf("Three");
			break;
		case 4: printf("Four");
			break;
		case 5: printf("Five");
			break;
		case 6: printf("Six");
			break;
		case 7: printf("Seven");
			break;
		case 8: printf("Eight");
			break;
		case 9: printf("Nine");
			break;
	}
}

return 0;
}