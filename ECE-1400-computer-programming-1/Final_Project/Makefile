RootTable: RootTable.o myLinkedList.o
	gcc -o RootTable RootTable.o myLinkedList.o

RootTable.o: RootTable.c myLinkedList.h
	gcc -c RootTable.c

myLinkedList.o: myLinkedList.c myLinkedList.h
	gcc -c myLinkedList.c