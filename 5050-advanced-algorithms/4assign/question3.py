class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.left_size = 0  # Size of the left subtree

def rank(root, x):
    # start at root of T
    if root is None:
        return 0

    # if x == curr.key
    if x == root.key:
        # return ++curr.left_size
        return root.left_size + 1

    # if x > curr.key
    if x > root.key:
        # add curr.left_size to rank and recurse with curr.right
        return root.left_size + 1 + rank(root.right, x)

    # if x < curr.key
    else:  # x < root.key
        # recurse with curr.left
        return rank(root.left, x)

# Helper function to insert a key in the BST
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
        root.left_size += 1
    elif key > root.key:
        root.right = insert(root.right, key)
    return root



# PRINT TREE
from collections import deque

def print_tree_by_level(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            print(node.key if node else 'None', end=" ")

            if node:
                queue.append(node.left)
                queue.append(node.right)
        print()
    print()

# Create a simple BST (not necessarily balanced in this example)
root = None
keys = [25, 16, 48, 8, 20, 59, 5, 18, 23]
for key in keys:
    root = insert(root, key)

print_tree_by_level(root)

# Test the rank function
keys += [60, 4, 49, 26, 19, 22]
for y in keys:
    print(f"The rank of {y} in the BST is: {rank(root, y)}")
