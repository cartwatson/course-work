#ifndef MYLINKEDLIST_H
#define MYLINKEDLIST_H

#define DEBUG

//define all prototypes

//declare structure for linked list
struct node{
	int input;
	float root2;
	float root3;
	float root4;
	struct node *next;
};

//search list
void search_list(FILE *input);

//print list
void printList(FILE *file);

//free list
void freeList(void);

#endif