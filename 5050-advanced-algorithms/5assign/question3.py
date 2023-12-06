def longest_increasing_subsequence(A, index=0, last=float('-inf'), memo={}):
    if index == len(A):
        return []

    key = (index, last)
    if key in memo:
        return memo[key]

    # Skip the current element
    skip = longest_increasing_subsequence(A, index + 1, last, memo)

    # Include the current element (if it forms an increasing subsequence)
    take = []
    if A[index] > last:
        take = [A[index]] + longest_increasing_subsequence(A, index + 1, A[index], memo)

    # Choose the longer subsequence
    memo[key] = max(skip, take, key=lambda x: len(x))
    return memo[key]


if __name__ == "__main__":
    A = [4, -2, 6, 7, 8, -100]
    B = [5, 4, 0, -2, 3, 6, 8, -100]
    print("Max Sum:", max_sum_common_subsequence(A, B))
