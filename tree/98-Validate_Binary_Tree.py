# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        def helper(root, minV, maxV):
            if not root: return True
            
            if root.val <= minV or root.val >= maxV: return False
                
            return helper(root.left, minV, root.val) and helper(root.right, root.val, maxV)
        
        return helper(root, float("-inf"), float("inf"))