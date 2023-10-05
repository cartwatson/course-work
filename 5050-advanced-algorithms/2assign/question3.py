def find_inversions(arr):
    # Initialize data structure to hold inversion pairs (list of tuples)
    inversions = []
    
    # Iterate over the array backwards
    for i in range(len(arr) - 1, 0, -1):
        # If the current element is less than the next element (iterating backwards)
        if arr[i] < arr[i - 1]:
            # Add pair to structure holding inversions
            inversions.append((arr[i - 1], arr[i]))
    
    # Return structure holding inversions
    return inversions

# Example usage:
arr = [4, 2, 9, 1, 7]
inversions = find_inversions(arr)
print(inversions)