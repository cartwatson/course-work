# is_k-smallest-element_smaller_than_x(A, n, k, x)
    # init count, nodes_to_search, curr_min=INT_MAX
    # add root to nodes_to_search
    # while nodes_to_search is not empty
        # get curr = nodes_to_search.pop(0)
        # increment count
        # if count equals or greater than k
            # if curr less than curr_min
                # store curr as curr_min
            
            # create temp = count, create power = 0
            # temp set to temp subtract 1
            # while temp greater than 0
                # temp set to temp subtract (2^power)
                # increment power
            # if temp equals 0
                # NOTE: count is a result of 2^x, therefore we have reached the end of the 
                # return (curr less than x)

        # add child nodes to nodes_to_search (if they exist)

from heapq import heapify


def is_kth_smallest_element_smaller_than_x(A, n, k, x):
    # Initialization
    add_children = True
    count = 0
    nodes_to_search = []
    curr_min = float('inf')  # Represents INT_MAX

    # Add root to nodes_to_search
    nodes_to_search.append(0)  # Assuming root is at index 0

    # While there are nodes to search
    while nodes_to_search:
        # Get current node
        curr_index = nodes_to_search.pop(0)
        curr_value = A[curr_index]
        count += 1

        # If count is equal to or greater than k
        if count >= k:
            add_children = False
            # Update curr_min if current value is smaller
            if curr_value < curr_min:
                curr_min = curr_value

        if add_children:
            # Add child nodes to nodes_to_search (if they exist)
            left_child_index = 2 * curr_index + 1
            right_child_index = 2 * curr_index + 2

            if left_child_index < n:
                nodes_to_search.append(left_child_index)
            if right_child_index < n:
                nodes_to_search.append(right_child_index)

    print("count: ", count)
    print("curr_min: ", curr_min)
    print("x: ", x)
    print(f"{curr_min} < {x}: ", curr_min < x)
    return curr_min < x


def main():
    # Example usage
    A = [2, 3, 4, 10, 11, 5, 16]
    heapify(A)  # Ensure the list is a heap
    print(A)
    k = 4
    x = 6
    is_kth_smallest_element_smaller_than_x(A, len(A), k, x)

if __name__ == "__main__":
    main()
