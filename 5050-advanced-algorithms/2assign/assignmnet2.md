# CS5050 -Assignment 2
Carter Watson

## Question 1
Suppose there are two sorted arrays A[1 ... n] and B[1 ... n], each having n elements (note that they may NOT be integers) sorted in ascending order.
Given a number x, we want to find an element A[i] from A and an element B[j] from B such that A[i] + B[j] = x, or report that no such two elements exist.
Design an O(n) time algorithm for the problem.

### Answer
```c++
// iterate forward over A - i
// iterate backward over B - j
// while iterating
    // if the sum of A[i] and B[j] == X
        // return the elements
    // elif the sum of A[i] and B[j] > X
        // decrement B's iterator
    // elif the sum of A[i] and B[j] < X
        // increment A's iterator
    // exit loop if iterators try to move out of array

// if exited loop then no result was found
    // report no loop was found
    // return
```

## Question 2
Your are given k sorted lists L1, L2, ..., Lk, with 1 ≤ k ≤ n, such that the total number of the elements in all k lists is n.
Note: Different lists may have different numbers of elements.

We assume that the elements in each sorted list Li, for any 1 ≤ i ≤ k, are already sorted in ascending order.
Design a divide-and-conquer algorithm to sort all these n numbers. Your algorithm should run in O(n log k) time (instead of O(n log n) time).

Note: An O(n log k) time algorithm would be better than an O(n log n) time one when k is sufficiently smaller than n.
For example, if k = O(log n), then n log k = O(n log log n), which is strictly smaller than n log n (i.e., n log log n = o(n log n)).

The following gives an example. There are five sorted lists (i.e., k = 5). Your algorithm needs to sort the
numbers in all these lists.
L1 : 3, 12, 19, 25, 36
L2 : 34, 89
L3 : 17, 26, 87
L4 : 28
L5 : 2, 10, 21, 29, 55, 59, 61

### Answer
```c++
// base case - only one list
    // return the one list

// function---merge lists of lists
// split the lists into two groups
// recursively merge the lists within each of the two groups by calling this function again on each of the split lists
// merge the two resulting lists from the recursive call
// return merged result

// function--merge two lists
// init array to return at end of function
// iterate over both lists from the beginning until one of the indexes hits the end of a list
    // if element from list1 is less than or equal to the element from list2
        // append the element of list1 to the end of the array to be returned
        // increment index for list1
    // else
        // append the element of list2 to the end of the array to be returned
        // increment index for list2

// append any remaining elements to array to be returned
// return array
```

## Question 3
Let A[1 · · · n] be an array of n distinct numbers (i.e., no two numbers are equal).
If i < j and A[i] > A[j], then the pair (A[i], A[j]) is called an inversion of A.

You are asked to answer the following questions.
(a) List all inversions of the array {4, 2, 9, 1, 7}.
(b) What array with elements from the set {1, 2, . . . , n} has the most inversions? How many inversions does it have?
(c) Give a divide-and-conquer algorithm that computes the number of inversions in array A in O(n log n) time. (Hint: Modify merge sort.) (20 points)

### Answer
(a)
- inversions: 
  - i=0 j=1 a[i]=4 a[j]=2
  - i=2 j=3 a[i]=9 a[j]=1
(b) The array with the most inversions would be an array where {INT_MAX, INT_MAX - 1, ..., negative INT_MAX}
(c) 
```c++
// init data structure to hold inverstion pairs (list of tuples) 
// iterate over the array backwards
    // if the current element is less than the next element (iterating backwards)
        // add pair to structure holding inversions
    // move to next element in array
// return structure holding inversions
```

## Question 4
Solve the following recurrences (you may use any of the methods we studied in class).
Make your bounds as small as possible (in the big-O notation). For each recurrence, T (n) = O(1) for n ≤ 1.
(a) T(n) = 2 · T (n / 2) + n^3
(b) T(n) = 4 · T ( n / 2 ) + n √n
(c) T(n) = 2 · T ( n / 2 ) + n log n
(d) T(n) = T ( 3n / 4 ) + n

### Answer
(a) O(n^3)
(b) O(n^2)
(c) O(n log^2 n)
(d) O(n log n)

## Question 5
You are consulting for a small computation-intensive investment company, and they have the following type of problem that they want to solve.

A typical instance of the problem is the following.
They are doing a simulation in which they look at n consecutive days of a given stock, at some point in the past.
Let’s number the days i = 1, 2, ..., n; for each day i, they have a price p(i) per share for the stock on that day.
(We’ll assume for simplicity that the price was fixed during each day)
Suppose during this time period, they wanted to buy 1000 shares on some day and sell all these shares on some (later) day.
They want to know: When should they have bought and when should they have sold in order to have made as much money as possible?
(If there was no way to make money during the n days, you should report this instead)

For example, suppose n = 5, p(1) = 9, p(2) = 1, p(3) = 5, p(4) = 4, p(5) = 7.
Then you should return “buy on 2, sell on 5”
(buying on day 2 and selling on day 5 means they would have made $6 per share, the maximum possible for that period)

Clearly, there is a simple algorithm that takes time O(n2): try all possible pairs of buy/sell days and see which makes them the most money.
Your investment friends were hoping for something a little better.

Design an algorithm to solve the problem in O(n log n) time. Your algorithm should use the divide-and-conquer technique

### Answer
```c++
// init data structure to hold current highest difference - init to the lowest possible value
// init current highest sell point as the last element in the list of days
// iterate over the array backwards
    // if the current element is the same as the next element (iterating backwards)
        // continue
    
    // if the current element is less than the next element 
        // store the next element as the current highest sell point

    // if the current element is more than the next element 
        // if the difference between the next element and the current highest sell point is higher than the current highest difference
            // store those elements as the current highest difference

    // move to next element in array

// return indexes of the highest differences
```