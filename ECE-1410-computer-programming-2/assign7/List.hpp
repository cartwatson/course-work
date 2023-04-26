#ifndef LIST_HPP
#define LIST_HPP

#include <string>
#include <sstream>
#include "Node.hpp"

#include <iostream> 

using namespace std;

template <typename T>
class List
{
  public:
    List()
    {
      //constructor
      head = nullptr;
      tail = nullptr;
    }

    //insert method
    void insert(T item)
    {
      //insert item at end
      //allocate new node
      Node<T>* temp = new Node<T>(item);
      //end of list set to null
      temp->setNext(nullptr); 
      //if first node
      if (head == nullptr)
      {
        //head and tail are set to temp
        head = temp;
        tail = temp;
      } else //not first node in list
      {
        tail->setNext(temp);
        tail = temp;
      }
    }
    

    //remove method
    void remove(T item) 
    {
      //loop through and remove item from every point in list
      
      //store head node
      Node<T>* prev;
      Node<T>* temp = head;
      //If head node itself holds the key or multiple occurrences of key
      while (temp != nullptr && temp->getData() == item)
      {
        head = temp->getNext();
        delete temp;
        temp = head;
      }
      //delete occurrences other than head
      while (temp != nullptr)
      {
        //search for item, keep track of previous node
        while (temp != nullptr && temp->getData() != item)
        {
          prev = temp;
          temp = temp->getNext();
        }

        //if item was not present
        if (temp == nullptr)
        {
          return;
        }

        //unlink the ndoe from linked list
        prev->setNext(temp->getNext());

        delete temp;

        //update temp
        temp = prev->getNext();

      }
    }

    //at method
    T at(int item)
    {
      //return item at that position
      //loop through until at that position
      int i = 0;
      Node<T>* last = head;
      while (last != nullptr)
      {
        if (i == item)
        {
          return last->getData();
        }
        i++;
        last = last->getNext();
      }
    }

    //count method
    int count()
    {
      //loop through list, return number of nodes
      //initialize counter
      int i = 0;
      Node<T>* p = head;
      //start for loop to go through list
      while (p != nullptr)
      {
        i++;
        if (p->getNext() != nullptr)
        {
          p = p->getNext();
        }
        else
        {
          break;
        }
        
      }
      //return counter when done
      return i;
    }

    //contains method
    bool contains(T item)
    {
      //loop through to check for item if found true
      //start loop
      Node<T>* p = head;
      while (p != nullptr)
      {
        //if data in p is equal to item
        if (p->getData() == item)
        {
            //return true
            return true;
        }
        p = p->getNext();
      }
      //if not returned then item not found
      //return false
      return false;
    }

    //toString method
    std::string toString()
    {
      //loop through and create string from each node
      //initialize message
      stringstream message;
      
      Node<T>* p = head;
      while (p != nullptr)
      {
          //add current data to message as a string
          T temp = p->getData();
          //convert to string and add
          message << temp << " ";

          p = p->getNext();
      }
      //return message
      return message.str();
    }
    
    //reset method
    void reset()
    {
      //remove everything in queue
      Node<T>* temp;
      while (head != tail)
      {
        temp = head;
        head = temp->getNext();
        free(temp);
      }
        temp = head;
        head = nullptr;
        delete temp;
    }

  private:
    Node<T>* head;
    Node<T>* tail;
};

#endif //LIST_HPP