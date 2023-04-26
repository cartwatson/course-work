#ifndef QUEUE_HPP
#define QUEUE_HPP

#include "Node.hpp"

template <typename T>
class Queue
{
    public:
        Queue()
        {
            //constructor
            pFront = nullptr;
            back = nullptr;
        }

        //enqueue method
        void enqueue(T item)
        {
            //place item at back of queue
            //create new node
            Node<T>* temp = new Node<T>(item);
            //attach new node to the list
            //if first node
            if(pFront == nullptr)
            {
                //pFront is set to new pointer
                pFront = temp;
                //back is set to new pointer
                back = temp;
                //attach node to front
                temp->setNext(back);
            } else //not first node in list
            {
                //attach last old node
                Node<T>* p = pFront;
                while (p->getNext() != nullptr)
                {
                    p = p->getNext();
                }
                //set old last node to point to new node
                p->setNext(temp);
                //set old tail to point to new node
                back = temp; 
            }
            //reset the end to null ptr
            temp->setNext(nullptr);
        }

        //dequeue method
        T dequeue()
        {
            // //remove and return front element (pop)
            // T temp = pFront->getData();
            // //change pFront
            // //create temporary new top var point it to the spot below current top
            // Node<T>* newFront = pFront->getNext();
            // //free current top
            // free(pFront);
            // //set pFront to point to the new top node
            // pFront = newFront;
            // //return data from old top node
            // return temp;

            T temp = pFront->getData();
            //create temporary currrent top var
            Node<T>* currFront = pFront;
            if (currFront->getNext() == 0 || currFront->getNext() == nullptr) //pop end of list
            {
                pFront = nullptr;
            } else { //poping not end of list
            //point it to the spot below current top
            pFront = currFront->getNext();
            }
            //free current front
            delete currFront;
            //return data from old top node
            return temp;
        }

        //front method
        T front()
        {
            //return but do NOT remove front element
            return pFront->getData();
        }

        //count method
        int count()
        {
            //loop through queue, return number of nodes
            //initialize counter
            int i =0;
            //start for loop to go through queue
            Node<T>* p = pFront;
            while (p != nullptr)
            {
                i++;
                p = p->getNext();
            }
            //return counter when done
            return i;
        }

        //reset method
        void reset()
        {
            //remove everything in queue
            Node<T>* temp;
            while (pFront != nullptr)
            {
                temp = pFront;
                pFront = temp->getNext();
                free(temp);
            }
        }

    private:
        Node<T>* pFront;
        Node<T>* back;
};

#endif //QUEUE_HPP