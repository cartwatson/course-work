# CS5050 - Assignment 3
Carter Watson

## Question 1
Suppose you are given an array A[1 ··· n], with each entry holding a distinct number (i.e., no two numbers of A are equal).
You are told that the sequence of values A[1], A[2], ..., A[n] is unimodal:
For some index p between 1 and n, the values in the array entries increase up to position p in A and then decrease the remainder of the way until position n.  

You would like to find the “peak entry” p without having to read the entire array – in fact, by reading as few entries of A as possible.
Show how to find the entry p by reading at most O(log n) entries of A.
In other words, design an O(log n) time algorithm to find the peak entry p.  

For example, let A = {1, 4, 6, 8, 11, 12, 10, 9, 7}, which is be a unimodal array. The peak entry of A is 12.
So the output of your algorithm may be either 12 or the index of 12 in A.

### Answer
```c++
// Algorithm FindPeak(A, low, high)
//     Input: A (array), low (starting index), high (ending index)
//     Output: peak value or index of peak value in array A

// if low > high
//     return "No peak found"  // Error case
// mid = (low + high) / 2
// if A[mid] < A[mid - 1]
//     return FindPeak(A, low, mid - 1)  // Search in the left half
// else if A[mid] < A[mid + 1]
//     return FindPeak(A, mid + 1, high)  // Search in the right half
// else
//     return mid
```

## Question 2
In the SELECTION algorithm we studied in class, the input numbers are divided into groups of five.
Will the algorithm still work in linear time if they are divided into groups of seven?
Please justify your answer

### Answer
```c++
// yes, the median of medians algorithm can be generalized to work with groups of seven
// The Median of Medians algorithm still works with groups of seven because dividing the data into groups of seven, finding the median of each group,
// and then finding the median of these medians serves the same purpose as with groups of five.
// It provides a good pivot for partitioning the array, ensuring that a significant fraction of elements are eliminated in each recursive step,
// which maintains the linear time complexity of the algorithm.
```

## Question 3
Suppose you are consulting for an oil company, which is planning a large pipeline (called the
main pipeline) running horizontally from east to west through an oil field of n wells.
From each well, a spur pipeline is to be connected directly to the main pipeline along a shortest path (going to either the north or the south), as shown in Figure 1  

Suppose there are n wells, represented by n points p1, p2, ..., pn in the plane.
We are given the x and y-coordinates of the n wells pi = (xi, yi) for i = 1, 2, ..., n.  

Note that the wells are not given in any sorted order.
Our goal is to pick an optimal location for the main pipeline (i.e., find the y-coordinate of the main pipeline) such that the total sum of the lengths of the spur pipelines is minimized. For simplicity, we assume that no two wells have the same x-coordinate or y-coordinate.  

Design an O(n) time algorithm to compute an optimal location for the main pipeline

### Answer
```c++
// put all y values in sorted list
// take median of list
// y value of main pipeline should be the median
```

## Question 4
Here is a generalized version of the selection problem, called multiple selection.  
Let A[1 ··· n] be an array of n numbers.
Given a sequence of m sorted integers k1, k2, ..., km, with 1 =< k1 < k2 < ··· < km =< n, the multiple selection problem is to find the ki-th smallest number in A for all i = 1, 2, ..., m.
For simplicity, we assume that no two numbers of A are equal.
For example, let A = {1, 5, 9, 3, 7, 12, 15, 8, 21}, and m=3 with k1 = 2, k2 = 5, and k3 = 7
Hence, the goal is to find the 2nd, the 5-th, and the 7-th smallest numbers of A, which are 3, 8, and 12, respectively.  

<ol type="a">
  <li>Design an O(n log n) time algorithm for the problem.</li>
  <li>Design an O(nm) time algorithm for the problem. Note that this is better than the O(n log n) time algorithm if m < log n.</li>
  <li>Improve your algorithm to O(n log m) time, which is better than both the O(n log n) time and the O(nm) time algorithms.</li>
</ol>

### Answer
```c++
// A
    // perform quick sort on the array - O(nlogn)
    // grab values with desired indeces - O(n)
    // return results
 
// B
    // Initialize an empty array - Result
    // For each index ki in K
        // Find the ki-th smallest element in A using QuickSelect
        // Append the found element to Result
    // Return Result

// C
    // Build a Balanced Binary Search Tree (BBST) from array A
    // Initialize an empty array - Result
    // For each index ki in K
    //     Find the ki-th smallest element in BBST
    //     Append the found element to Result
    // Return Result

```

## Question 5
Implement the SELECTION algorithm in Python, the one with the order of O(n), including the
sophisticated pivot selection strategy.
Your implementation should take an array A and k as the input and return k-th smallest element.
A should be a general array of real numbers. A can have duplicates too.

Test your algorithm’s running time with various sizes of A and different ks.  

### Answer
```python
def median_of_medians(A, i):

    # Divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        # Base case
        pivot = sorted(medians)[len(medians)//2]
    else:
        # Recursive call
        pivot = median_of_medians(medians, len(medians)//2)

    # Partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i - k - 1)
    else:  # pivot = k
        return pivot
```
