# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:   
#         if not root: return True
        
#         def helper(left, right):
#             if not left and not right: return True
#             if not left or not right: return False
            
#             if left.val == right.val:
#                 return helper(left.left, right.right) and helper(left.right, right.left)
#             else:
#                 return False
            
#         return helper(root.left, root.right)


    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        if not root.left and not root.right: return True
        if not root.left or not root.right: return False
        
        stack = [root.left, root.right]
        
        while stack:
            # print([n.val for n in stack])
            l = stack.pop()
            r = stack.pop()
            
            if l.val != r.val: return False
            
            if l.left and r.right:
                stack.append(l.left)
                stack.append(r.right)
            elif l.left or r.right:
                return False
            
            if l.right and r.left:
                stack.append(l.right)
                stack.append(r.left)
            elif l.right or r.left:
                return False
            

        return True