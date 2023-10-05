def find_highest_difference(arr):
    # Initialize data structure to hold current highest difference - init to the lowest possible value
    highest_difference = float('-inf')
    highest_difference_indexes = (0, 0)
    
    # Initialize current highest sell point as the last element in the list of days
    highest_sell_point = arr[-1]
    highest_sell_point_index = len(arr) - 1

    # Iterate over the array backwards
    for i in range(len(arr) - 2, -1, -1):  # start at the second to last element, stop at 0
        # If the current element is the same as the next element (iterating backwards)
        if arr[i] == arr[i + 1]:
            continue

        # If the current element is less than the next element
        if arr[i] < arr[i + 1]:
            # Store the next element as the current highest sell point
            highest_sell_point = arr[i + 1]
            highest_sell_point_index = i + 1

        # If the current element is more than the next element
        elif arr[i] > arr[i + 1]:
            # If the difference between the next element and the current highest sell point is higher than the current highest difference
            difference = highest_sell_point - arr[i + 1]
            if difference > highest_difference:
                # Store those elements as the current highest difference
                highest_difference = difference
                highest_difference_indexes = (i + 1, highest_sell_point_index)

    # Return indexes of the highest differences
    return highest_difference_indexes

# Example usage:
arr = [9, 1, 5, 4, 7]
indexes = find_highest_difference(arr)
print(indexes)
