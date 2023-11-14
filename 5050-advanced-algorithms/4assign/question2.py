class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_smallest_val_geq_x(curr, x):
    # Base case: If the current node is None, return None
    if curr is None:
        return None

    # If the current node's key is equal to x, return x
    if curr.key == x:
        return x

    # If the current node's key is greater than x
    if curr.key > x:
        # Check in the left subtree
        left_result = find_smallest_val_geq_x(curr.left, x)
        # Return the smaller of the two values
        return min(curr.key, left_result) if left_result is not None else curr.key

    # If x is greater than the current node's key, search in the right subtree
    return find_smallest_val_geq_x(curr.right, x)

# Helper function to insert a key in the BST
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
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

def main():
    # Create a simple BST
    root = None
    keys = [15, 10, 20, 8, 12, 16, 25]
    for key in keys:
        root = insert(root, key)

    # print for funsies
    print("BST level by level:")
    print_tree_by_level(root)

    # Test the function
    x = 8
    result = find_smallest_val_geq_x(root, x)
    print(f"The smallest value in the BST greater than or equal to {x} is: {result}")

if __name__ == "__main__":
    main()
