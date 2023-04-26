/***************************************************************************************
	Function title: Final Program
	Author: Jethro Watson
	
	Inputs: input file
	Outputs: output file
	
	Summary: Takes integers from input.txt, calculates square, cube, and fourth roots, 
			 and outputs values to output.txt
	
	Compile Instructions: Use Makefile

****************************************************************************************
								PSEUDOCODE (main)
BEGIN
	READ NUMBERS OUT OF INPUT FILE
		IGNORE DUPLICATES
	SORT NUMBERS (smallest to largest)
		USE LINKED LIST
	DYNAMICALLY ALLOCATE MEMORY
	CALCULATE SQUARE, CUBE, AND FOURTH ROOTS
	OUTPUT NUMBER AND ROOTS TO OUTPUT FILE
		USE PROPER SPACING
	FREE MEMORY
	TERMINATE PROGRAM
END
***************************************************************************************/


#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "myLinkedList.h"

//main function
int main(int argc, const char *argv[])
{
	#ifdef DEBUG
	printf("Entered main function\n");
	#endif
	
	//initialize variables
	struct node *prev = NULL;	//used in sorting
	struct node *curr = NULL; 	//used in sorting and freeing memory
	struct node *new_node;		//node pointer
	FILE *input, *output; 		//i/o file pointers
	int fileInput;				//used to add to list and check for EOF
	int closeCheck;				//used to check if files closed
	
	//check for errors
	//exit if incorrect number of agruments are passed
	if (argc != 3) 
	{
		//print exit code
		printf("Not enough command line arguments\n");
		exit(1);
	}
	
	#ifdef DEBUG
	printf("passed argc error\n");
	#endif
	
	//try to open input and output files
	input = fopen(argv[1], "r");
	output = fopen(argv[2], "w");
	//if successful
	if (input != NULL && output != NULL) {
		//continue	
	} else { //else
		//error
		printf("The files could not be opened correctly.\n");
		//exit
		exit(2);
	}
	
	//while EOF character not found in input file
	while (1)
	{
		//if end of file, break
		if(feof(input)) {
			#ifdef DEBUG
			printf("reached EOF\n");
			#endif
			break;
		}
		
		//Search for correct spot
		search_list(input);
	}
	

	//send num and roots to output file
	printList(output);
	//page 437
	
	//close files
	fclose(input);
	fclose(output);

	//check to see if input closed properly
	if (closeCheck != 0) 
	{
		printf("Input file failed to close\n");
		exit(1);
	} else {
		#ifdef DEBUG
		printf("Input file closed\n");
		#endif
	}
	closeCheck = fclose(output);
	//check to see if output closed properly
	if (closeCheck != 0) 
	{
		printf("Output file failed to close\n");
		exit(1);
	} else {
		#ifdef DEBUG
		printf("Output file closed\n");
		#endif
	}
	
	//free memory
	//page 436
	freeList();
	
	return 0;
}