class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

def find_values(curr: TreeNode, values: list, lower_bound: int, upper_bound: int):
    # Check if current node exists
    if curr is None:
        return

    # if curr.left.key >= lower_bound
    # Note: Also check if curr.left exists before accessing its key
    if curr.left and curr.left.key >= lower_bound:
        find_values(curr.left, values, lower_bound, upper_bound)

    if lower_bound <= curr.key <= upper_bound:
        print("appending", curr.key)
        values.append(curr.key)

    # if curr.right.key <= upper_bound
    # Note: Also check if curr.right exists before accessing its key
    if curr.right and curr.right.key <= upper_bound:
        find_values(curr.right, values, lower_bound, upper_bound)

# Example usage
root = TreeNode(25)
root.left = TreeNode(16)
root.right = TreeNode(48)
root.left.left = TreeNode(8)
root.left.left.left = TreeNode(5)
root.left.right = TreeNode(20)
root.left.right.left = TreeNode(18)
root.left.right.right = TreeNode(23)
root.right.right = TreeNode(59)

# lower_bound = x_l, upper_bound = x_r
lower_bound = 10
upper_bound = 26

# init empty list - values
values = []

# find_values(root, values, lower_bound, upper_bound)
find_values(root, values, lower_bound, upper_bound)

# for value in values:
sum=0
for value in values:
    sum += value
    # print(value)
    print(value)

print("sum: ", sum)
