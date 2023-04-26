/***************************************************************************************
	Function title: Program 10
	Author: Jethro Watson
	
	Inputs: Command Line
	Outputs: Print to screen
	
	Summary: Program takes string input from command line determines which string would
			 come first and which would come last if the strings were placed in
			 dictionary order the first and last in dictionary order are printed
	
	Compile Instructions: gcc program10_project1.c -o program10.exe

****************************************************************************************
									PSEUDOCODE
BEGIN
	INTIALIZE VARIABLES
	INTIALIZE ARRAY
	COMPARE FIRST TWO ARGUMENTS
		USE strcmp TO DETERMINE ARGUMENTS WITH LARGEST ASCII VALUES
		ASSIGN LARGEST TO ARRAY largest
		ASSIGN SMALLEST TO ARRAY smallest
	DETERMINE LARGEST AND SMALLEST ARGUMENTS
		USE strcmp TO DETERMINE ARGUMENTS WITH LARGEST ASCII VALUES
		ASSIGN LARGEST TO ARRAY largest
		ASSIGN SMALLEST TO ARRAY smallest
		REPEAT UNTIL ALL ARGUMENTS HAVE BEEN PROCESSED
	PRINT LARGEST AND SMALLEST ARGUMENTS
END
***************************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define DEBUG

int main(int argc, const char *argv[])
{
	//intialize variables
	int i, j, l, s;
	//intialize arrays
	char largest[20];
	char smallest[20];

	
	//compare first two arguments
	j = strcmp(argv[i], argv[++i]);
	// if argv[i] is greater put it as largest and argv[++i] as smallest
	if (j > 0)
	{
		// is argv[i] greater
		strcpy(largest, argv[i]);
		strcpy(smallest, argv[++i]);
	} else {
		// is argv[++i] greater
		strcpy(largest, argv[++i]);
		strcpy(smallest, argv[++i]);
	}
	

	//repeat first comparison with rest of the arguments
	for(i=1; i<argc; i++)
	{
		l = strcmp(argv[i], largest);
		s = strcmp(argv[i], smallest);

		if (l > 0)
		{
		strcpy(largest, argv[i]);
		}
		if (s < 0)
		{
		strcpy(smallest, argv[i]);
		}
	}
	
	//print smallest and largest words
	printf("Smallest word: %s\n", smallest);
	printf("Largest word: %s\n", largest);
}