def solve_knapsack(size, items, memo):
    if size in memo:
        return memo[size]

    for item in items:
        if size == item:
            memo[size] = True
            return memo[size]
        elif size - item < 0:
            memo[size] = False
            return memo[size]
        return solve_knapsack(size-item, items, memo)

if __name__ == "__main__":
    M = 14
    items = [2, 7, 9, 3]

    # M = 1
    # items = [2, 3, 4]

    print(f"M: {M}\nitems: {items}\nsolution: {solve_knapsack(M, items, {})}")
