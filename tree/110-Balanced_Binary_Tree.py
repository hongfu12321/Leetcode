# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            
            if l == -1 or r == -1: return -1
            return max(l, r) + 1 if abs(l - r) <= 1 else -1
        
        return helper(root) != -1

'''
Runtime: 40 ms, faster than 97.83% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 19.1 MB, less than 25.83% of Python3 online submissions for Balanced Binary Tree.
'''