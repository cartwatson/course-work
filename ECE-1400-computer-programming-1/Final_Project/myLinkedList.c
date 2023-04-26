#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "myLinkedList.h"
//head pointer
struct node *head = NULL; 	//first node in list


/*************************************************
				search_list
BEGIN
	progress through list unless value is less 
	than or equal to the next value
	if value is equal to n do not add to list
END
*************************************************/
void search_list(FILE *input)
{		
	//initialize variables
	struct node *curr, *prev, *new_node;
	
	//allocate memory
	new_node = malloc(sizeof(struct node));
	//check to see if allocation failed
	if (new_node == NULL) {
		printf("Malloc failed.\n");
		return;
	}
	
	fscanf(input, "%d", &new_node->input);
	#ifdef DEBUG
	printf("fileInput: %d\n", new_node->input);
	#endif
	
	//move through list
	for (curr = head, prev = NULL;
		 curr != NULL && new_node->input > curr->input;
		 prev = curr, curr = curr->next)
		;
	
	//check to see if value already exists
	if (curr != NULL && new_node->input == curr->input) {
		printf("Value %d already exists\n", new_node->input);
		free(new_node);
		return;
	}
	
	//calculate values
	new_node->root2 = sqrt(new_node->input);
	new_node->root3 = cbrt(new_node->input);
	new_node->root4 = pow(new_node->input, 0.25);
	
	new_node->next = curr;
	if (prev == NULL) {
		head = new_node;
	} else {
		prev->next = new_node;
	}
}

/*************************************************
				printList
BEGIN
	print list
		with proper formatting
END
*************************************************/
void printList(FILE *fp) 
{
	struct node *p;
	
	fprintf(fp, "Input\tSquare\tCube\tFourth\n");
	#ifdef DEBUG
	printf("Head: %d\n", head != NULL);
	#endif
	for (p = head; p != NULL; p = p->next) 
	{
		printf("%d\t%.4f\t%.4f\t%.4f\n", p->input, p->root2, p->root3, p->root4);
		fprintf(fp, "%d\t%.4f\t%.4f\t%.4f\n", p->input, p->root2, p->root3, p->root4);
	}
}

/*************************************************
				freeList
BEGIN
	free list
END
*************************************************/
void freeList(void)
{
	struct node *curr;
	
	while ((curr = head) != NULL) 
	{
		//advance first to next element
		head = head->next;
		//free previous node
		free(curr);                
	}
} 