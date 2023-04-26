#include <stdio.h>
#include <stdlib.h>

#include "stack.h"

/*************************************
		read_RPN
BEGIN
	INTIALIZE VARIABLES
	switch
		case 0
			push 0
		case 1
			push 1
		case 2
			push 2
		case 3
			push 3
		case 4
			push 4
		case 5
			push 5
		case 6
			push 6
		case 7
			push 7
		case 8
			push 8
		case 9
			push 9
		case +
			pop operand1
			pop operand2
			add operands
		case -
			pop operand1
			pop operand2
			subtract operands
		case *
			pop operand1
			pop operand2
			multiply operands
		case /
			pop operand1
			pop operand2
			divide operands
		case 
			print result of pop()
END
*************************************/
void read_RPN(char ch){
	int operand1, operand2;
	
	switch(ch){
		case '0':
			push(0);
			break;
		case '1':
			push(1);
			break;
		case '2':
			push(2);
			break;
		case '3':
			push(3);
			break;
		case '4':
			push(4);
			break;
		case '5':
			push(5);
			break;
		case '6':
			push(6);
			break;
		case '7':
			push(7);
			break;
		case '8':
			push(8);
			break;
		case '9':
			push(9);
			break;
			
		case '+':
			operand2 = pop();
			operand1 = pop();
			push(operand1 + operand2);
			break;
		case '-':
			operand2 = pop();
			operand1 = pop();
			push(operand1 - operand2);
			break;
		case '*':
			operand2 = pop();
			operand1 = pop();
			printf("operand1: %d\n", operand1);
			printf("operand2: %d\n", operand2);
			push(operand1 * operand2);
			break;
		case '/':
			operand2 = pop();
			operand1 = pop();
			push(operand1 / operand2);
			break;
			
		case '=':
			printf("The value of this expression is: %d", pop());
			break;
			
		case ' ':
			break;
	}
	
}

/*****************************
			main
BEGIN
	INTIALIZE VARIABLES
	READ RPN EXPRESSION
	CALL READ_RPN
END
*****************************/
int main(void) {
	char ch;

		printf("Enter an RPN expression: ");
		while ((ch = getchar()) != EOF && ch != '\n') {
			read_RPN(ch);
		}
	
	return 0;
}