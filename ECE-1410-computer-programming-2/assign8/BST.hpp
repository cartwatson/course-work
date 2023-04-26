#ifndef BST_HPP
#define BST_HPP

#include <string>
#include <sstream>
#include "Node.hpp"
#include "Queue.hpp"

template <typename T>
class BST
{
    public:
        BST()
        {
            //constructor
            root = nullptr;
        }

        //insert method
        void insert(T item)
        {
            //insert item into tree
            //create new node
            Node<T>* temp = new Node<T>(item);
            //set left and right of temp
            temp->setLeft(nullptr);
            temp->setRight(nullptr);
            //check to see if first node
            if (root == nullptr) //first node
            {
                //point head to new node
                root = temp;
                //exit
                return;
            }

            //loop through
            Node<T>* p = root;
            while (p != nullptr)
            {
                if (p->getData() == item) //is item
                {
                    //dont duplicate node
                    //exit
                    return;
                }
                if (p->getData() < item) //greater than item
                {
                    if (p->getRight() != nullptr) //check to make sure not at end
                    {
                        //move to the right
                        p = p->getRight();
                    }
                    else
                    {
                        //if it is nullptr then break
                        break;
                    }
                }
                else //less than item
                {
                    if (p->getLeft() != nullptr) //check to make sure not at end
                    {
                        //move to the left
                        p = p->getLeft();
                    }
                    else
                    {
                        //if it is nullptr then break
                        break;
                    }
                }
            }

            //assign new node
            //p is just before null at this point
            if (p->getData() < item) //insert at right
            {
                p->setRight(temp);
            }
            else //insert at left
            {
                p->setLeft(temp);
            }


        }

        //contains method
        bool contains(T item)
        {
            //search for item return true if found
            //go through tree using pointers to try to find item
            Node<T>* p = root;
            while (p != nullptr)
            {
                if (p->getData() == item) //p is item
                {
                    return true;
                }
                if (p->getData() < item) //right
                {
                    p = p->getRight();
                }
                else //left
                {
                    p = p->getLeft();
                }
            }

            //if not already returned, return false
            return false;
        }

        //search method
        std::string search(T item)
        {
            //search tree for item
            //keep track of path
            bool found = false;
            std::stringstream path;
            std::stringstream messageFinal;
            //add path to string
            path << "root(" << root->getData() << ")";

            //loop through
            Node<T>* p = root;
            while (p != nullptr)
            {
                if (p->getData() == item) //p is item
                {
                    found = true;
                    break;
                }
                if (p->getData() < item) //right
                {
                    p = p->getRight();
                    if (p == nullptr)
                        break;
                    path << "->right(" << p->getData() << ")";
                }
                else //left
                {
                    p = p->getLeft();
                    if (p == nullptr)
                        break;
                    path << "->left(" << p->getData() << ")";
                }
            }

            //final changes to streams            
            if (found) //found item
            {
                //if found then "Found: " += path
                messageFinal << "Found: ";
                messageFinal << path.str();
                return messageFinal.str();
            }
            else //item not found
            {
                //if !found then "Not Found: " += path
                messageFinal << "Not found: ";
                messageFinal << path.str();
                return messageFinal.str();
            }
            
        }

        //count method
        int count()
        {
           //initialize variables
           int count = 0;
            Node<T>* p = root;
            Queue<Node<T>*> myQueue;
            myQueue.enqueue(root);
            while (p != nullptr)
            {
                //check branches
                if (p->getLeft() != nullptr)
                {
                    //add to list
                    myQueue.enqueue(p->getLeft());
                }
                if (p->getRight() != nullptr)
                {
                    //add to list
                    myQueue.enqueue(p->getRight());
                }
                //take from list
                //set list to node popped
                p = myQueue.dequeue();
                //increase counter
                count++;
                //repeat until null
            }
            //return counter
            return count;
        }

    private:
        Node<T>* root;
};

#endif //BST_HPP