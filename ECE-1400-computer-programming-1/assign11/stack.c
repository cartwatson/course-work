#include <stdio.h>
#include <stdlib.h>

#include "stack.h"

#define STACK_SIZE 100


int contents[STACK_SIZE];
int top = 0;

/*************************************
		make_empty
BEGIN
	SET THE TOP OF THE STACK TO ZERO
END
*************************************/
void make_empty(void){
	top = 0;
}

/*************************************
		is_empty
BEGIN
	IF stack is empty
		RETURN TRUE (1)
	ELSE
		RETURN FALSE (0)
END
*************************************/
int is_empty(void){
	return top == 0;
}

/*************************************
		is_full
BEGIN
	IF stack is full
		RETURN TRUE (1)
	ELSE
		RETURN FALSE (0)
END
*************************************/
int is_full(void){
	return top == STACK_SIZE;
}

/*************************************
		stack_overflow
BEGIN
	PRINT Too many operators and/or operands
END
*************************************/
void stack_overflow(void){
	printf("Too many operators and/or operands");
}

/*************************************
		stack_underflow
BEGIN
	PRINT Too few operators and/or operands
END
*************************************/
void stack_underflow(void){
	printf("Too few operators and/or operands");
}

/*************************************
			push
BEGIN
	IF stack is full
		RETURN stack_overflow
	ELSE
		place int on top of stack
END
*************************************/
void push(int i){
	if (is_full()){
		stack_overflow();
	} else {
		contents[top++] = i;
	}
}

/*************************************
			pop
BEGIN
	IF stack is empty
		RETURN stack_underflow
	ELSE
		return and remove top of stack
END
*************************************/
char pop(void){
	if (is_empty()){
		stack_underflow();
	} else {
		return contents[--top];
	}
}