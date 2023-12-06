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


if __name__ == "__main__":
    A = [20, 5, 14, 8, 10, 3, 12, 7, 16]
    ayo = longest_increasing_subsequence(A)
    print(ayo)
    print()
    if ayo == [5, 8, 10, 12, 16]:
        print("IT WORKS")
    else:
        print(":(")