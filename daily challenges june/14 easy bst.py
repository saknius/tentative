"""
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between
the values of any two different nodes in the tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def min_abs_diff_in_bst(root):
    stack = []
    curr = root
    prev = None
    min_diff = float('inf')

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        if prev is not None:
            diff = abs(curr.value - prev.value)
            min_diff = min(min_diff, diff)

        prev = curr
        curr = curr.right

    return min_diff
