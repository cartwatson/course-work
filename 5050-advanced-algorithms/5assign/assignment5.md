# Assignment 5

Carter Watson  
CS5050 - AdvAlg  
Due NOV 17 2023  

## Question 1

Given a knapsack of size M and n items of sizes {a1, a2, ..., an}, determine whether there is a subset S of the items such that the sum of the sizes of all items in S is exactly equal to M . We assume M and all item sizes are positive integers.  

Here we consider the following unlimited version of the problem. The input is the same as before, except that there is an unlimited supply of each item. Specifically, we are given n item sizes a1, a2, . . . , an, which are positive integers. The knapsack size is a positive integer M . The goal is to find a subset S of items (to pack in the knapsack) such that the sum of the sizes of the items in S is exactly M and each item is allowed to appear in S multiple times.

For example, consider the following sizes of four items: {2, 7, 9, 3} and M = 14. Here is a solution for the problem, i.e., use the first item once and use the fourth item four times, so the total sum of the sizes is 2 + 3 × 4 = 14 (alternatively, you may also use the first item 2 times, the second item one time, and the fourth item one time, i.e., 2 × 2 + 7 + 3 = 14).

Design an O(nM) time dynamic programming algorithm for solving this unlimited knapsack problem. For simplicity, you only need to determine whether there exists a solution (namely, you answer is just “yes” or “no”; if there exists a solution, you do not need to report an actual solution subset).

## Answer

```python
# function takes params
#   size=M
#   items=items (has length of n)
#   memo=dictionary (starts as empty if not provided)
def solve_knapsack(size, items, memo={}):
    # check memo to see if we've done this problem before, return if we have
    if size in memo:
        return memo[size]

    # this keeps the time complexity to O(n) for the algorithm
    for item in items:
        # check for base cases
        if size == item:
            memo[size] = True
            return memo[size]
        # check for case where answer is False
        elif size - item < 0:
            memo[size] = False  
            return memo[size]
        # create recursive subproblems
        return solve_knapsack(size-item, items, memo)

# start problem and print True/False==Yes/No
result = solve_knapsack(M, items)
print(result)
```

### Subproblems

The subproblem for this particular case is similar to the original problem but with a reduction in the size of the knapsack equal to the item just put in the knapsack.

### Dependency Relationship

This algorithm takes a top down approach, it attempts to solve problems by starting with the maximum size, and slowly reducing that size as it moves through subproblems.  It also has a lot of overlapping subproblems, there exist scenarios where two subproblems will both attempt to solve a knapsack of the same size with the same items, this is why adding memoization speeds up the program significantly.  The base cases are: when the size of the knapsack is equal to an item, which has a return value of True, and when the previous condition is False and the size of the knapsack minus the current item is less than zero, which has a return value of False.

### Time Complexity

The time complexity of this algorithm is O(nM) because the algorithm loops over n values in a scenario where all items fit in the knapsack.  And has M subproblems that can spawn from these loops of n.  Therefore the overall complexity is O(nM).


## Question 2

Here is another variation of the knapsack problem. We are given n items of sizes a1, a2, ..., an, which are positive integers. Further, for each 1 <= i <= n, the i-th item ai has a positive value value(ai) (you may consider value(ai) as the amount of dollars the item is worth). The knapsack size is a positive integer M.

Now the goal is to find a subset S of items such that the sum of the sizes of all items in S is at most M and the sum of the values of all items in S is maximized.

Note that each item can be used at most once in this problem.

Design an O(nM) time dynamic programming algorithm for the problem. For simplicity, you only need to report the sum of the values of all items in the optimal solution subset S and you do not need to report the actual subset S.

## Answer

restate the problem
need to maximize sum of items in knapsack

```python
def solve_knapsack(size: int, items: list[Item], memo={}, sum_val=0) -> int:
    # catch base case of no items left, or size is too small
    if not items:
        return sum_val

    if size <= 0:
        return sum_val
    
    # cant index dict with list because it's not hashable, create key instead
    key = (size, tuple(item for item in items))

    # we've already solved this exact problem
    if key in memo:
        return memo[key]

    max_value = sum_val
    for item in items:
        # if item fits in bag
        if size - item.weight >= 0:
            # create a new list of items without the current item in it
            new_list = items.copy()
            new_list.remove(item)
            # solve the subproblem
            answer = solve_knapsack(size-item.weight, new_list, memo, sum_val+value(item))
            max_value = max(max_value, answer)
        
    # store and return result
    memo[key] = max_value
    return memo[key]
```

### Subproblems

The subproblem is similar to the first question, each subproblem has a unique set of items and size.  Those are the two qualifiers for what defines the uniqueness of the subproblem which is why it is used to build the key for the memoization.

### Dependency Relationship

This solution takes a top down approach to solving the weighted/valued knapsack problem.  It slowly reduces the size of the knapsack based on which item is the most valuable.  It takes advantage of overlapping subproblems by using memoization.

### Time Complexity

The time complexity for this algorithm is the same as the first problem as it follows the same basic structure.  Refer to answer 1.


## Question 3

In class, we studied the longest common subsequence problem. Here we consider a similar problem, called maximum-sum common subsequence problem, as follows.

Let A be an array of n numbers and B another array of m numbers (they may also be considered as two sequences of numbers). A maximum-sum common subsequence of A and B is a common subsequence of the two arrays that has the maximum sum among all common subsequences of the two arrays (see the example given below).

As in the longest common subsequence problem studied in class, a subsequence of elements of A (or B) is not necessarily consecutive but follows the same order as in the array.

Note that some numbers in the arrays may be negative.

Design an O(nm) time dynamic programming algorithm to find the maximum-sum common subsequence of A and B. For simplicity, you only need to return the sum of the elements in the maximum-sum common subsequence and do not need to report the actual subsequence.

## Answer

```python
def max_sum_common_subsequence(A, B, index_A=0, index_B=0, memo={}):
    # catch base case of either index out of range
    if index_A >= len(A) or index_B >= len(B):
        return 0

    # create key
    key = (index_A, index_B)

    # we've already solved this exact problem
    if key in memo:
        return memo[key]

    # if elements match, move forward in both lists
    if A[index_A] == B[index_B] and A[index_A] > 0:
        result = A[index_A] + max_sum_common_subsequence(A, B, index_A + 1, index_B + 1, memo)
    else:
        # if elements don't match, make two calls
        # move foward the index of opposite lists for each call
        skip_A = max_sum_common_subsequence(A, B, index_A + 1, index_B, memo)
        skip_B = max_sum_common_subsequence(A, B, index_A, index_B + 1, memo)
        # only keep the result of the larger list
        result = max(skip_A, skip_B)

    # Memoize and return result
    memo[key] = result
    return result
```


### Subproblems

The subproblem for this situation is defined by the indices of the lists.

### Dependency Relationship

This approach solves the max sum common subsequence working from the back of the lists to the front.  Its very similar to the other approaches I've taken in this assignment. It shares similarities to a depth first search, it will drill down as deep as it can go into the problem and slowly build up the max sum common subsequence. 

### Time Complexity

The time complexity on this algorithm is the same as the complexity for any of the other algorithms discussed in this assignment for the same reason.  They all take the same approach.


## Question 4

Given an array A[1 . . . n] of n distinct numbers (i.e., no two numbers of A are equal), design an O(n2) time dynamic programming algorithm to find a longest monotonically increasing subsequence of A (see the definition below). Your algorithm needs to report not only the length but also the actual longest
subsequence (i.e., report all elements in the subsequence).

Here is a formal definition of a longest monotonically increasing subsequence of A (refer to the example given below). The subsequence of A is a subset of numbers of A such that if a number a appears in front of another number b in the subsequence, then a is also in front of b in A (i.e., the subsequence follows the same order as in A). Next, a subsequence of A is monotonically increasing if for any two numbers a and b such that a appears in front of b in the subsequence, a is smaller than b. Finally, a longest monotonically increasing subsequence of A refers to a monotonically increasing subsequence of A that is the longest (i.e. has the maximum number of elements) among all monotonically increasing subsequences of A.

For example, if A = {20, 5, 14, 8, 10, 3, 12, 7, 16}, then a longest monotonically increasing subsequence is 5, 8, 10, 12, 16.

Note that the answer may not be unique, in which case you only need to report one such longest subsequence.

## Answer

```python
def longest_increasing_subsequence(A, index=0, last=float('-inf'), memo={}):
    # catch base case where we are at the end of the array
    if index == len(A):
        return []

    # create key
    key = (index, last)

    # we've already solved this exact problem
    if key in memo:
        return memo[key]

    # we have two options, skip or take the current element
    # let both play out, assuming it's possible to take based on previous element
    skip = longest_increasing_subsequence(A, index + 1, last, memo)
    take = []
    if A[index] > last:
        take = [A[index]] + longest_increasing_subsequence(A, index + 1, A[index], memo)

    # only save longer subsequence
    memo[key] = max(skip, take, key=lambda x: len(x))
    return memo[key]
```

### Subproblems

The problems here are defined by the current index and the last value taken.

### Dependency Relationship

This algorithm builds from the back to the front, like the last algorithm.  It builds the subsequence by either skipping or taking the current element and then returning whatever subsequence is longer.

### Time Complexity

The algorithm is O(n^2) because it goes over the whole list twice.  Once in its main call but also because it forms n number of branched processes.
