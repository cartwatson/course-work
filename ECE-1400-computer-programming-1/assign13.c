/***************************************************************************************
	Function title: Program 13
	Author: Jethro Watson

	Inputs: User
	Outputs: Print to screen

	Summary: user inputs a word, input is added to list, program stops adding words when
			 user inputs blank word, words are sorted and printed

	Compile Instructions: Use Visual Studio

****************************************************************************************
									PSEUDOCODE
									   main
BEGIN
	INTIALIZE VARIABLES
	START LOOP TO GET WORDS FROM USER
		ASK USER FOR WORDS
		IF WORD IS BLANK
			BREAK
		ENDIF
		DYNAMICALLY SIZE ARRAY
		COPY wordtemp INTO temp
		EXPAND list TO FIT temp
		ADD WORD TO LIST
		INCREASE COUNTER
	INTIALIZE didswap
	START BUBBLE SORT
		START INNER SORT
		IF list[n] > list[n+1]
			SWAP VIA TEMPS
			REASSIGN didswap
		END IF
	PRINT list
END
								read_line
BEGIN
	IF getchar() != '\n'
		GET CHARACTER AND PLACE INTO LIST
	ELSE
		RETURN LIST
END
***************************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEBUG

int read_line(char str[], int n);

int main(void) {
	//intialize variables
	int i;
	int n;
	int didSwap;
	int wordCount = 0;
	char wordtemp[21];
	char* temp = NULL;
	char* temp1 = NULL;
	char* temp2 = NULL;
	char* word = NULL;
	char** list = NULL;

	//start loop to get words from user
	for (i = 0; ; i++) {
		//ask user for words
		printf("Enter word: ");
		read_line(wordtemp, 21);
		
		#ifdef DEBUG
		printf("scanf complete\n");
		printf("%s\n", wordtemp);
		#endif


		//if word is blank break from loop and sort
		if (wordtemp[0] == '\0') {
			#ifdef DEBUG
			printf("vibe check failed\n");
			#endif
			break;
		} 

		#ifdef DEBUG
		printf("vibe check passed\n");
		printf("strlen: %d\n", strlen(wordtemp));
		#endif

		//make array dynamically sized
		temp = malloc(sizeof(wordtemp));

		#ifdef DEBUG
		printf("temp realloc complete\n");
		#endif

		//copy contents into temp
		strcpy_s(temp, 21, wordtemp);

		#ifdef DEBUG
		printf("temp copy complete\n");
		#endif

		
		//expand list to fit word
		list = (char**) realloc(list, sizeof(list)+sizeof(char *));
		list[i] = (char*) malloc(sizeof(temp));

		#ifdef DEBUG
		printf("list realloc complete\n");
		#endif

		#ifdef DEBUG
		printf("temp: %s\n", temp);
		#endif

		//add word to list
		list[i] = temp;

		#ifdef DEBUG
		printf("word added to list\n");
		#endif

		//increase counter
		wordCount++;

		#ifdef DEBUG
		printf("current word count: %d\n", wordCount);
		#endif

		#ifdef DEBUG
		printf("word: %s\n\n", list[i]);
		#endif
	}

	#ifdef DEBUG
	printf("out of input\n");
	#endif

	temp2 = (char*)malloc(21);
	temp1 = (char*)malloc(21);

	//intialize did swap to true
	didSwap = 1;
	//start bubble sort
	while (didSwap) {
		didSwap = 0;
		
		#ifdef DEBUG
		printf("entered while loop\n");
		#endif

		//start inner sort 
		for (n = 0; n < sizeof(list)-1; n++) {
			#ifdef DEBUG
			printf("entered for loop\n");
			#endif
			if (list[n] > list[n+1]) {
				#ifdef DEBUG
				printf("entered switch if\n");
				#endif
				//swap items via temps
				temp2 = list[n];
				#ifdef DEBUG
				printf("passed pof 1\n");
				#endif
				temp1 = list[n+1];
				#ifdef DEBUG
				printf("passed pof 2\n");
				printf("temp2: %s\n", temp2);
				printf("temp1: %s\n", temp1);
				#endif

				list[n] = (char *) realloc(list[n], sizeof(temp2));
				if (list[n] == NULL) {
					exit(1);
				}
				list[n + 1] = (char*) realloc(list[n + 1], sizeof(temp1));
				if (list[n + 1] == NULL) {
					exit(2);
				}
				#ifdef DEBUG
				printf("passed pof 3\n");
				#endif

				strcpy_s(list[n], sizeof(list[n]), temp1);
				strcpy_s(list[n+1], sizeof(list[n + 1]), temp2);
				#ifdef DEBUG
				printf("list[n]: %s\n", *(list + n));
				printf("list[n+1]: %s\n", *(list + n + 1));
				#endif
				//reassign didSwap
				didSwap = 1;
			}
		}
	}

	//print sorted list
	printf("In sorted order: ");
	for (i = 0; i < wordCount; i++) {
		#ifdef DEBUG
		printf("printing\n");
		#endif
		printf("%s", *(list + i));
	}
}



int read_line(char str[], int n)
{
	int ch, i = 0;

	while ((ch = getchar()) != '\n')
		if (i < n)
			str[i++] = ch;
	str[i] = '\0';
	return i;
}