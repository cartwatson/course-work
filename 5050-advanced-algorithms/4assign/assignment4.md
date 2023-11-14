# Assignment 4

Carter Watson  
CS5050 - AdvAlg  
Due NOV 10 2023  

## Question 1
Suppose we have a min-heap with n distinct keys that are stored in an array A[1 ... n] (a min-heap is one that stores the smallest key at its root). Given a value x and an integer k with 1 <= k <= n, design an algorithm to determine whether the k-th smallest key in the heap is smaller than x (so your answer should be “yes” or “no”). The running time of your algorithm should be O(k), independent of the size of the heap.

NOTE: If we were to find the k-th smallest key of the heap, denoted by y, then the best way would be to perform k times deleteMin operations, which would take O(k log n) time (or using the selection algorithm, which would take O(n) time). Our above problem, however, is actually a decision problem. Namely, you only need to decide whether y is smaller than x, and you do not have to know what the exact value of y is. Hence, the problem is easier and we are able to solve it in a faster way, i.e., O(k) time.

### Answer

#### Algorithm Explanation

Perform a depth first search, keep track of the number of elements encountered, when a node is larger than x, don't include it on the number of elements encountered and don't move forward with this section of the dfs.  If you reach k encountered nodes and it is smaller than x, you know that x is larger than the k-th smallest element due to the nature of min-heaps.

#### Time Analysis

This algorithm works in O(k + C) time (where C is a constant that is not larger than k), which is dominated by the linear time of k, therefore the algorithm is O(k) time.  C is guaranteed to be smaller than K because C is just the nodes that are touched but not counted, this is guarnteed to be smaller than k due to the nature of dfs on trees.

## Question 2

Suppose you are given a balanced binary search tree T of n nodes (as discussed in class, each node v has v.left, v.right, and v.key). We assume that no two nodes of T have the same key. Given a value x, the successor of x in T is defined as follows:

1. If x is larger than every key in T , then x does not have a successor
2. if x is equal to a key in T, then the successor of x is x itself
3. otherwise, the successor of x is the smallest key of T that is larger than x.

Design an O(log n) time algorithm to perform the successor operations: Given any value x, your algorithm should return the successor of x in T, and return “NULL” if x does not have a successor in T.

### Answer

1. Give answer in psuedocode  
```c++
// start at root of T
// init smallest_val to INT_MAX
// do this part recursively - init with root - curr is current node
    // if x == curr.key
        // return x
    // if curr.key > x
        // if smallest_val > curr.key
            // smallest_val = curr.key
    // if x > curr.key
        // compare to root.right
    // if x < curr.key
        // compare to root.left

// if smallest_val != INT_MAX
    // return smallest_val
// else
    // return NULL
```

#### Algorithm Explaination

The algorithm is just a recursive search through a binary tree, it starts at the root node.  It will move to the right node if x is greater than the current key, and to the left if x is smaller than the current key.  Before it moves it will first check to see if x is equal to the current key and if it is it will return x ("if x is equal to a key in T, then the successor of x is x itself").  Then it will check to see if the current key is greater than x, if it is the algorithm checks to see if the current key is the smallest value yet seen that is larger than x, if that is the case, then it will store the current value as the smallest value yet seen.  After recursively moving through the tree, if smallest value has been set, return that value, otherwise return NULL.

#### Time Analysis

The time complexity for this algorithm is at worst O(log n) due the nature of the search algorithm for balanced binary trees.  This is because at the worst case X is larger than the entire tree therefore the algorithm must traverse the entire height of the tree which is logn.

## Question 3

Suppose you are given a balanced binary search tree T of n nodes (as discussed in class, each node v has v.left, v.right, and v.key). We assume that no two keys in T are equal. Given a value x, the rank operation rank(x) is to return the rank of x in T , which is defined to be one plus the number of keys of T smaller than x.  

For example, if T has 3 keys smaller than x, then rank(x) = 4. Note that x may or may not be a key in T. For example, in Figure 1, rank(16) = 3, rank(21) = 6, rank(25) = 7, rank(26) = 8. We know that T can support the ordinary search, insert, and delete operations, each in O(log n) time.

You are asked to augment T , such that the rank operation, as well as the normal search, insert, and delete operations, all take O(log n) time each

### Answer

1. the design of your data structure (i.e., how you augment T)
The augment will be to store the size of the left subtree at each node

1. the algorithm for implementing the rank(x) operation (please give the pseudocode)
```c++
// find_rank(curr, x)
    // if curr doesn't exist
        // return 0

    // if x equals curr.key
        // return curr.left.size + 1

    // if x greater than curr.key
        // return curr.left.size + 1 + find_rank(curr.right, x)
    
    // if x less than curr.key
        // return find_rank(root.left, x)

// start at root of T
// return find_rank(root, x)
```

3. briefly explain why the normal operations search, insert, and delete can still be performed in O(log n) time each (you do not need to provide the details of these operations).  
Search is unaffected by the additional information, because it only reads information it doesn't have to do any extra and can act as if the left_size was not there.  Insert and Delete remain in O(log n) time because the left_size can be updated as they perform as normal.  When insert or delete moves over a node they will have to update the left_size of that node based on where it moves.  Rebalancing after inserting or deleting will take more time than normal but only modifies the constant in front of O(log n), therefore while technically slower it is still O(log n) and shouldn't be drastically affected.

## Question 4

This problem is concerned with range queries (we have discussed a similar problem in class) on a balanced binary search tree T whose keys are distinct (no two keys in T are equal). The range query is a generalization of the ordinary search operation. The range of a range query on T is defined by a pair [x_l, x_r], where x_l and x_r are real numbers and x_l <= x_r. Note that x_l and x_r may not be the keys in T.

You already know that T can support the ordinary search, insert, and delete operations, each in O(log n) time, where n is the number of nodes of T . You are asked to design an algorithm to efficiently perform the range queries. That is, in each range query, you are given a range [x_l, x_r], and your algorithm should report all keys x stored in T such that x_l <= x <= x_r. Your algorithm should run in O(k + log n) time, where k is the number of keys of T in the range [x_l, x_r]. In addition, it is required that all keys in [x_l, x_r] be reported in a sorted order.

NOTE: Such an algorithm of O(k + log n) time is an output-sensitive algorithm because the running time (i.e., O(k + log n)) is a function of the output size k. As an application of the range queries, suppose the keys of T are student scores in an exam. A range query like [70, 80] would report all scores in the range in sorted order.

### Answer

1. Please give the pseudocode for your algorithm.
```c++
// NOTE: this is assuming curr.left and curr.right exist, those will need to be checked for but doing so doesn't add time complextity
// def find_values(curr, values, lower_bound, upper_bound)
    // if curr.left.key >= lower_bound
        // find_values(curr.left, values, lower_bound, upper_bound)

    // if lower_bound <= curr.key >= upper_bound
        // values.append(curr.key)

    // if curr.right.key <= upper_bound
        // find_values(curr.right, values, lower_bound, upper_bound)

// init empty list - values 
// lower_bound = x_l
// upper_bound = x_r
// find_values(root, values, lower_bound, upper_bound)
// for value in values:
    // print(value)
```

#### Algorithm Explaination

The find_values algorithm will recursively move over the balance BST. In doing so it will try to chase down the lowest value in the BST that is above or equal to the lower bound.  Then it will check to see if the current node is in range, adding it to the values if it is.  If the right node is below the upper bound it will then recursively move through the right subtree.  Moving throught the tree in this specific order guarantees that the values in range appear in a sorted order.

#### Time Complexity

The algorithm is O(k + logn). This is because the search operation to find the a node in range is O(logn) which comes from the height of a balanced BST.  Then we have to get K nodes around it leading us to a final time complexity of O(k + logn).

## Question 5

Consider one more operation on the above balanced binary search tree T in Problem 4: range-
sum(x_l, x_r). Given any range [x_l, x_r] with x_l <= x_r, the operation range-sum(x_l, x_r) computes the sum of the keys in T that are in the range [x_l, x_r].

You are asked to augment the binary search tree T , such that the range-sum(x_l, x_r) operations, as well as the ordinary search, insert, and delete operations, all take O(log n) time each. 

### Answer

1. the design of your data structure (i.e., how you augment T)
In each node we store the sum of the subtree of each node

2. the algorithm for implementing the range-sum(x_l, x_r) operation (please give the pseudocode)
```c++
// NOTE: this is assuming curr.left and curr.right (and curr.left.right, curr.right.left)exist, those will need to be checked for but doing so doesn't add time complextity
// def range_sum(curr, sum, lower_bound, upper_bound)
    //// calculate sum
    // if checked_nodes does not contain curr.left
        // if curr.key >= lower_bound and curr.left.key >= lower_bound 
            // sum += curr.left.right.sum
            // checked_nodes.append(curr.left.right)
            // range_sum(curr.left, sum, lower_bound, upper_bound)
    
    // if checked_nodes does not contain curr.right
        // if curr.key <= upper_bound and curr.right.key <= upper_bound 
            // sum += curr.right.left.sum
            // checked_nodes.append(curr.right.left)
            // range_sum(curr.right, sum, lower_bound, upper_bound)

    //// traverse the tree
    // if curr.key > upper_bound
        // range_sum(curr.left, sum, lower_bound, upper_bound)

    // if curr.key < lower_bound
        // range_sum(curr.right, sum, lower_bound, upper_bound)

    //// add node itself
    // if checked_nodes does not contain curr.left
        // if curr.key <= lower_bound and curr.key >= upper_bound
            // sum += curr.key

// init sum to 0
// init checked_nodes to empty list
// range_sum(root of T, sum, lower_bound, upper_bound)
```
#### Algorithm Explanation

The algorithm is essentially looking for chunks of the tree that are guaranteed to be in range and thus it can take advantage of already having the sum precalculated.

#### Time Analysis

The algorithm is O(logn) as it is essentially following the same steps as problem 4 but it doesn't have to actually look at k values so it's much more efficient, changing the time complexity from O(k + logn) where k is the number of values summed, to O(logn).

3. briefly explain why the ordinary operations search, insert, and delete can still be performed in O(log n) time each (you do not need to provide the details of these operations)  
Search is unaffected by the additional information, because it only reads information it doesn't have to do any extra and can act as if the sum was not there.  Insert and Delete remain in O(log n) time because the sum can be updated as they perform as normal.  When insert or delete moves over a node they will have to update the sum of that node based on where it moves.  Rebalancing after inserting or deleting will take more time than normal but only modifies the constant in front of O(log n), therefore while technically slower it is still O(log n) and shouldn't be drastically affected.
