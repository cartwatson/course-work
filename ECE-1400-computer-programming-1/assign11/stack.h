#ifndef STACK_H
#define STACK_H

//define all prototypes

//Empty the stack
void make_empty(void);

//Returns true if stack is empty
int is_empty(void);

//Returns true if stack is full
int is_full(void);

//Pushes integer i onto the top of the stack
void push(int i);

//Removes the top item from the stack and returns it
char pop(void);

#endif