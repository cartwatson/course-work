#ifndef STACK_HPP
#define STACK_HPP

#include "Node.hpp"

template <typename T>
class Stack
{
    public:
        Stack()
        {
            //constructor
            pTop = nullptr;
        }

        //push method
        void push(T item)
        {
            //"push" item on top of stack
            //create new node
            Node<T>* newTop = new Node<T>(item);
            //make new node reference old head
            newTop->setNext(pTop);
            pTop = newTop;
        }

        //pop method
        T pop()
        {
            //remove and return top element of stack
            T temp;
            temp = pTop->getData();
            //create temporary currrent top var
            Node<T>* currTop = pTop;
            if (currTop->getNext() == 0 || currTop->getNext() == nullptr) //pop end of list
            {
                pTop = nullptr;
                free(currTop);
            } else { //poping not end of list
            //point it to the spot below current top
            pTop = currTop->getNext();
            //free current top
            free(currTop);
            }

            //return data from old top node
            return temp;
        }

        //top method
        T top()
        {
            //return top without removing it from stack
            return pTop->getData(); 
        }

        //count method
        int count()
        {
            //return number of elements in stack
            //initialize var
            int i = 0;
            Node<T>* p = pTop;
            while (p != nullptr)
            {
                i++;
                p = p->getNext();
            }
            //return i (Counter)
            return i;
        }

        //reset method
        void reset()
        {
            //remove everything in queue
            Node<T>* temp;
            while (pTop != nullptr)
            {
                temp = pTop;
                pTop = temp->getNext();
                free(temp);
            }
        }

    private:
        Node<T>* pTop;
};


#endif //STACK_HPP