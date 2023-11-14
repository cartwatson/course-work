class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.sum = key

def insert(node, key):
    if node is None:
        return TreeNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.sum = node.key
    if node.left is not None:
        node.sum += node.left.sum
    if node.right is not None:
        node.sum += node.right.sum

    return node

def range_sum(curr: TreeNode, sum, lower_bound, upper_bound):
    if (curr is None):
        return sum

    print("curr.key: ", curr.key, curr.sum)

    # if curr.key and curr.left are both greater than or equal to lower_bound
    if curr.left:
        if (curr.key >= lower_bound) and (curr.left.key >= lower_bound):
            sum += curr.left.right.sum if curr.left.right else 0
            range_sum(curr.left, sum, lower_bound, upper_bound)
    
    # if curr.key and curr.right are both less than or equal to upper_bound
    if curr.right:
        if (curr.key <= upper_bound) and (curr.right.key <= upper_bound):
            sum += curr.right.left.sum if curr.right.left else 0
            range_sum(curr.right, sum, lower_bound, upper_bound)

    if curr.key > upper_bound:
        print("moving_left")
        range_sum(curr.left, sum, lower_bound, upper_bound)

    if curr.key < lower_bound:
        print("moving_right")
        range_sum(curr.right, sum, lower_bound, upper_bound)

    # # if curr.key in lower and upper bound
    if lower_bound <= curr.key and curr.key <= upper_bound:
        print("adding: ", curr.key)
        sum += curr.key

    return sum

# Example usage
root = TreeNode(25)
values = [16, 48, 8, 20, 59, 5, 18, 23]
for val in values:
    root = insert(root, val)

# lower_bound = x_l, upper_bound = x_r
lower_bound = 10
upper_bound = 26

print("lower_bound: ", lower_bound)
print("upper_bound: ", upper_bound)

# find_values(root, values, lower_bound, upper_bound)
sum = range_sum(root, 0, lower_bound, upper_bound)

print("sum: ", sum)
