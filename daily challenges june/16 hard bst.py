"""
1569. Number of Ways to Reorder Array to Get Same BST
Given an array nums that represents a permutation of integers from 1 to n.
We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST.
Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3],
we will have 2 as the root, 1 as a left child, and 3 as a right child.
The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

"""
# construct a binary search tree
from math import comb
from typing import List
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.bst_insert(data, self.root)

    def bst_insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.bst_insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.bst_insert(data, node.right)
        else:
            return

    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.data, end=" ")
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data, end=" ")
    
    def preorder_traversal(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)

    def numOfWays(self, nums) -> int:
        tree = BinarySearchTree()
        n = len(nums)
        for i in range(n):
            tree.insert(nums[i])
        tree.inorder_traversal(tree.root)

        return 
    
    def buildtree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildtree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildtree(preorder[mid+1:], inorder[mid+1:])
        return root
    
    def KthSmallest(self, root, k):
        """
        Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        """
        if not root:
            return None
        if k == 1:
            return root.data
        self.KthSmallest(root.left, k-1)
        self.KthSmallest(root.right, k-1)
        return root.data
    
    def KthSmallest2(self, root, k):
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.data
            curr = curr.right

    def KthSmallest3(self, root, k):
        if not root:
            return None
        if k == 1:
            return root.data
        
        left_count = count_nodes(root.left)
        if k <= left_count:
            return self.KthSmallest3(root.left, k)
        elif k == left_count + 1:   
            return root.data
        else:
            return self.KthSmallest3(root.right, k - left_count - 1)
    

    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left) + len(right), len(right)) * f(left) * f(right)
        
        return (f(nums) - 1) % (10**9 + 7)
    
    

    

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
    

tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(9)
# print('inorder')
# tree.inorder_traversal(tree.root)
# print('postorder')
# tree.postorder_traversal(tree.root)
# print('preorder')
# tree.preorder_traversal(tree.root)
# tree.numOfWays([3,2,1,4,5])
tree.KthSmallest(tree.root,1)
tree.KthSmallest2(tree.root,1)
tree.KthSmallest3(tree.root,1)
print(tree.KthSmallest(tree.root,1))
print(tree.KthSmallest2(tree.root,5))
print(tree.KthSmallest3(tree.root,5))