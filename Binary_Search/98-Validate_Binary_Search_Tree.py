'''
BT-98-Validate Binary Search Tree

Medium

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

 
Example 1:

        2
       / \
      1   3
    
    Input: [2,1,3]
    Output: true

Example 2:

        5
       / \
      1   4
         / \
        3   6
    
    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.


note:
- Every node value at the left subtree would always less than the root value.
- Same as the right subtree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST_recursion(self, root: TreeNode) -> bool:     
        def helper(node, minV=float('-inf'), maxV=float('inf')):
            if not node: return True
            if node.val <= minV or node.val >= maxV: return False
            
            return helper(node.left, minV, node.val) and \
                    helper(node.right, node.val, maxV)
    
        return helper(root) 

    
    def isValidBST_iterate(self, root: TreeNode) -> bool:     
            nodeList = []
            minV = float('-inf')
            while root or nodeList:
                while root:
                    nodeList.append(root)
                    root = root.left
                root = nodeList.pop()

                if root.val <= minV: return False
                minV = root.val
                root = root.right
            
            return True