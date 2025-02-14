public class BinarySearchTree<T extends Comparable<T>> {
    //create static node class to use in tree
    static class Node<T> {
        //initialize variables
        T data;
        //point to child nodes
        Node<T> left = null;
        Node<T> right = null;
    }

    //create static queue class to use in count method
    static class Queue<T> {
        //initialize variables
        Node<T> front = null;
        Node<T> back = null;
        //enqueue method
        public void enqueue(T item) {
            //place item at back of queue
            //create new node
            Node<T> temp = new Node<>();
            temp.data = item;
            //attach new node to the list
            //if first node
            if(front == null) {
                //pFront is set to new pointer
                front = temp;
                //back is set to new pointer
                back = temp;
                //attach node to front
                temp.right = back;
            } else {//not first node in list
                //attach last old node
                Node<T> p = front;
                while (p.right != null) {
                    p = p.right;
                }
                //set old last node to point to new node
                p.right = temp;
                //set old tail to point to new node
                back = temp;
            }
            //reset the end to null ptr
            temp.right = null;
        }

        //dequeue method
        public T dequeue() {
            //create temporary current top var
            Node<T> currFront = front;
            //if nothing in queue, break
            if (currFront == null) {
                return null;
            }
            //pop end of list
            if (currFront.right == null) {
                front = null;
            } else { //popping not end of list
                //point it to the spot after current front
                front = currFront.right;
            }
            //return new front
            if (front != null)
            {
                return front.data;
            }
            else
            {
                return null;
            }
        }
    } //end class queue

    //initialize class variable
    public Node<T> root = null;

    //insert method for BST class
    public boolean insert(T Value) {
        /*
        insert value into tree
        no duplicates
        if already in tree return false
        insert item into tree
        */

        //create new node
        Node<T> temp = new Node<>();
        temp.data = Value;
        //check to see if first node
        if (root == null) { //first node
            //point root to new node
            root = temp;
            //exit
            return true;
        }

        //loop through
        Node<T> p = root;
        while (true) {
            //is value
            if (p.data == Value) {
                //don't duplicate node
                //exit
                return false;
            }
            //less than value
            if (p.data.compareTo(Value) < 0) {
                ///check to make sure not at value
                if (p.right != null) {
                    //move to the right
                    p = p.right;
                } else {
                    //if it is nullptr then break
                    break;
                }
            } else { //less than Value
                //check to make sure not at end
                if (p.left != null) {
                    //move to the left
                    p = p.left;
                } else {
                    //if it is nullptr then break
                    break;
                }
            }
        }

        //assign new node
        //p is just before null at this point
        if (p.data.compareTo(Value) < 0) { //insert at right
            p.right = temp;
        } else { //insert at left
            p.left = temp;
        }

        return true;
    }

    //remove method for BST class
    boolean remove(T value) {
        /*
        deletes value from tree
        if value was in tree and deleted return true
        */
        if (!this.search(value)) {
            return false;
        }

        //loop through to find node to be deleted
        Node<T> toBeDeleted = root;
        Node<T> parent = null;
        while (toBeDeleted.data != value) {
            //change parent node before changing toBeDeleted
            parent = toBeDeleted;
            //less than value
            if (toBeDeleted.data.compareTo(value) < 0) {
                //move to the right
                toBeDeleted = toBeDeleted.right;
            } else { //less than Value
                //move to the left
                toBeDeleted = toBeDeleted.left;
            }
        } //to be deleted in on node that needs to be deleted

        //has no left child
        if (toBeDeleted.left == null) {
            //find child
            Node<T> child = toBeDeleted.right;
            //test to see if only one node
            if (parent == null) {
                root = toBeDeleted.right;
            } else {
                //assign branch of parent to child
                if (parent.data.compareTo(value) < 0) {
                    parent.right = child;
                } else {
                    parent.left = child;
                }
            }
        } else { //has left child
            //find rightmost
            Node<T> rightMost = toBeDeleted.left;
            Node<T> parentRightMost = toBeDeleted;
            while (rightMost.right != null) {
                //change parent node before changing toBeDeleted
                parentRightMost = rightMost;
                //is value
                rightMost = rightMost.right;
            } //rightMost at right most
            //copy rightMost value into node to be deleted
            toBeDeleted.data = rightMost.data;
            //connect correct link of parent to rightMost to left link of rightMost
            if (parentRightMost.right == rightMost) {
                parentRightMost.right = rightMost.left;
            }
            if (parentRightMost.left == rightMost) {
                parentRightMost.left = rightMost.left;
            }
        }
        //return true
        return true;
    }


    //search method for BST class
    boolean search(T value) {
        /*
        searches returns true if found
        go through tree using pointers to try to find item
        */

        Node<T> p = root;
        while (p != null) {
            //p is value
            if (p.data == value) {
                return true;
            }
            //right
            if (p.data.compareTo(value) < 0) {
                p = p.right;
            } else { //left
                p = p.left;
            }
        }

        //if not already returned, return false
        return false;
    }

    //display method for BST class
    void display(String message) {
        /*
        performs an in-order traversal of the tree
        displaying the value at each node
        add message display first
        */

        //message display
        System.out.println(message);
        //in order list of names

    }

    //numberNodes method for BST class
    int numberNodes() {
        /* counts all nodes in tree */
        //initialize variables
        int count = 0;
        Node<T> p = root;
        Queue<Node<T>> myQueue = new Queue<>();
        myQueue.enqueue(root);
        while (p != null) {
            //check branches
            if (p.left != null) {
                //add to list
                myQueue.enqueue(p.left);
            }
            if (p.right != null) {
                //add to list
                myQueue.enqueue(p.right);
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

    //numberLeafNodes method for BST class
    int numberLeafNodes() {
        /*counts all leaf nodes */
        //initialize variables
        int count = 0;
        Node<T> p = root;
        Queue<Node<T>> myQueue = new Queue<>();
        myQueue.enqueue(root);
        while (p != null) {
            //check to see if leaf
            if (p.left != null && p.right != null) {
                //increase counter
                count++;
            }

            //check branches
            if (p.left != null) {
                //add to list
                myQueue.enqueue(p.left);
            }
            if (p.right != null) {
                //add to list
                myQueue.enqueue(p.right);
            }
            //take from list
            //set list to node popped
            p = myQueue.dequeue();
            //repeat until null
        }
        //return counter
        return ++count;
    }

    //height method for BST class
    int height() {
        /* returns height */
        return __height(root);
    }

    private int __height(Node<T> p)
    {
        //base case
        if (p == null) {
            return 0;
        } else {
            int rightDepth = 0;
            int leftDepth = 0;

            if (p.left == null) {
                rightDepth = __height(p.right);
            }
            if (p.right == null) {
                leftDepth = __height(p.left);
            }

            //recursively call __height to calculate depth of both trees
            if (p.right != null && p.left != null) {
                leftDepth = __height(p.left);
                rightDepth = __height(p.right);
            }

            //return larger depth
            if (leftDepth > rightDepth) {
                return (leftDepth);
            } else {
                return (rightDepth);
            }
        }
    }
}
