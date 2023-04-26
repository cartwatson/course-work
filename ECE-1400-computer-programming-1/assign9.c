/*****************************************************************************************
	Function title: Program 2b
	Author: Jethro Carter Watson
	
	Inputs: User
	Outputs: Print to screen
	
	Summary: 
	
	Compile Instructions: gcc program9_project2b.c -o project2b.exe

*******************************************************************************************
									PSEUDOCODE
BEGIN
	ITNIALIZE ARRAY AND VARIABLES
	FILL FIRST ARRAY WITH MESSAGE FROM USER
		TERMINATE ARRAY IF USER INPUTS ENTER
		IF AN INPUTTED CHARACTER IS NOT PART OF THE ALPHABET, IGNORE IT
		MAKE ALL INPUTTED CHARACTERS UPPERCASE
	REVERSE THE ARRAYS
	CHECK EACH VALUE OF BOTH ARRAYS AGAINST EACH OTHER TO DETERMINE IF THEY ARE THE SAME
	IF ALL VALUES ARE THE SAME MESSAGE IS A PALINDROME
		PRINT "Your message is a palindrome!"
	ELSE
		PRINT "Your message is not a palindrome"
END
******************************************************************************************/

#include <stdio.h>

#define N 500

int main() {
	//intialize variable
	char a[N], r[N], *p, *k; 
	int i, j, c;

	//fill first array
	printf("Input message: ");
	for (p = a, i = 0; p < a + N;) {
		//get message from user
		scanf("%c", p);
		
		//terminate array when user inputs enter
		if(*p == '\n'){
			*p = '\0';
			break;
		}
		
		//if charcater is not a alphabetical character do not save it
		if((*p >= 'A' && *p <= 'Z') || (*p >= 'a' && *p <= 'z')){
			//make current char uppercase for verification purposes
			if (*p >= 'a' && *p <= 'z') {
				*p -= 32;
			}
			p++;
			i++;
		}
	}
	
	//place the reverse of a into r
	for (p = a + i - 1, k = r; p >= a; p--, k++) {
		*k = *p; 
	}
		
	//check arrays for similarities
	for (p = a, k = r, c = 0; i > c; c++, p++, k++) {
		//if *k == *p increment j to later verify against i
		if (*k == *p) {
			j++;
		}
	}
	
	//tell user whether message is a palindrome or not
	if (j == i) {
		printf("Your message is a palindrome!");
	} else {
		printf("Your message is not a palindrome");
	}
}