class Item:
    def __init__(self, w, v):
        self.value: int = v
        self.weight: int = w

    def __str__(self):
        return f"Item(weight={self.weight}, value={self.value})"


def value(item: Item) -> int:
    return item.value

def print_items(items: list[Item]) -> None:
    print("items:")
    for item in items:
        print(item)

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
        if size - item.weight >= 0:
            new_list = items.copy()
            new_list.remove(item)
            answer = solve_knapsack(size-item.weight, new_list, memo, sum_val+value(item))
            max_value = max(max_value, answer)
        
    memo[key] = max_value
    return memo[key]

if __name__ == "__main__":
    M = 14
    items: list[Item] = [Item(2, 2), Item(7, 3), Item(9, 4), Item(3, 5)]    
    
    print(f"Sum: {solve_knapsack(M, items)}")
