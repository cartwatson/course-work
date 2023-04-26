/***************************************************************************************
	Function title: Program 9
	Author: Jethro Watson

	Inputs: none
	Outputs: Print to screen

	Summary: Program generates a random walk around a 10x10 array

	Compile Instructions:

****************************************************************************************
									PSEUDOCODE
BEGIN
	INTIALIZE VARIABLES
	INTIALIZE 10x10 ARRAY
	FILL ARRAY WITH PERIODS
	CREATE RANDOM SEED
	START PROGRAM IN UPPER LEFT HAND CORNER
	RANDOMIZE DIRECTION
		CHECK IF DIRECTION IS VALID
			IF NOT CHOOSE NEW DIRECTION
			IF ALL DIRECTIONS ARE BLOCKED SKIP TO PRINT ARRAY
	MOVE IN DIRECTION AND PRINT NEXT CHAR
	CONTINUE UNTIL Z IS PRINTED TO LETTER IS TRAPPED
	FINISH ARRAY
	PRINT ARRAY
END
***************************************************************************************/

#include <stdio.h>

#define COL 10
#define ROW 10

int main()
{
	//intialize variables
	int i, j, n;
	int direction;
	int row;
	int col;
	int blocked = 0;
	char trappedLetter = 0;
	int isTrapped = 0;

	row = 0;
	col = 0;

	//intialize array
	char a[ROW][COL];

	//fill array with periods
	for (i = 0; i < ROW; i++) {
		for (j = 0; j < COL; j++) {
			a[i][j] = ".";
		}
	}

	//create random seed
	srand((unsigned)time(NULL));

	//start in left hand corner
	a[row][col] = "A";

	//generate the rest of the letters
	for (n = "B"; n <= "Z"; n++) {

		//get direction
		direction = (rand() % 4);

		//put letter in adjacent cell
		switch (direction) {
		case 0: //north
			//north
			if ((row - 1 >= 0) && (a[row - 1][col == "."])) {
				a[--row][col] = n;
				break;
			}
			else
			{
				blocked++;
			}

			//south
			if ((row + 1 <= 9) && (a[row + 1][col] == ".")) {
				a[++row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			//east
			if ((col + 1 <= 9) && (a[row][col + 1] == ".")) {
				a[row][++col] = n;
				break;
			}
			else {
				blocked++;
			}

			//west
			if ((col - 1 >= 0) && (a[row][col - 1] == ".")) {
				a[row][--col] = n;
				break;
			}
			else {
				blocked++;
			}
			break;

		case 1: //east
			//east
			if ((col + 1 <= 9) && (a[row][col + 1] == ".")) {
				a[row][++col] = n;
				break;
			}
			else {
				blocked++;
			}

			//west
			if ((col - 1 >= 0) && (a[row][col - 1] == ".")) {
				a[row][--col] = n;
				break;
			}
			else {
				blocked++;
			}

			//north
			if ((row - 1 >= 0) && (a[row - 1][col] == ".")) {
				a[--row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			//south
			if ((row + 1 <= 9) && (a[row + 1][col] == ".")) {
				a[++row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			break;

		case 2: //south
			//south
			if ((row + 1 <= 9) && (a[row + 1][col] == '.')) {
				a[++row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			//north
			if ((row - 1 >= 0) && (a[row - 1][col] == '.')) {
				a[--row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			//east
			if ((col + 1 <= 9) && (a[row][col + 1] == '.')) {
				a[row][++col] = n;
				break;
			}
			else {
				blocked++;
			}

			//west
			if ((col - 1 >= 0) && (a[row][col - 1] == '.')) {
				a[row][--col] = n;
				break;
			}
			else {
				blocked++;
			}

			break;
		case 3: //west
			//west
			if ((col - 1 >= 0) && (a[row][col - 1] == '.')) {
				a[row][--col] = n;
				break;
			}
			else {
				blocked++;
			}

			//east
			if ((col + 1 <= 9) && (a[row][col + 1] == '.')) {
				a[row][++col] = n;
				break;
			}
			else {
				blocked++;
			}

			//north
			if ((row - 1 >= 0) && (a[row - 1][col] == '.')) {
				a[--row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			//south
			if ((row + 1 <= 9) && (a[row + 1][col] == '.')) {
				a[++row][col] = n;
				break;
			}
			else {
				blocked++;
			}

			break;
		}

		//all directions are blocked, skip to end
		if (blocked == 4) {
			isTrapped = 1;
			trappedLetter = --n;
			break;
		}

		//reset blocked for next letter
		blocked = 0;

	}

	//print array
	printf("\n");

	for (i = 0; i < ROW; i++) {
		for (j = 0; j < COL; j++) {
			printf("%c ", a[i][j]);
		}
		printf("\n");
	}