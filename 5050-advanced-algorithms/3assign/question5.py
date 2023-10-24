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

if __name__ == "__main__":
    # Example Usage:
    A = [10, 3, 2, 1, 14, 12, 17, 19, 10, 6, 11, 5]
    k = 5  # looking for the 6th smallest element (0-based index)
    result = median_of_medians(A, k)
    print(result)  # Output: 10
