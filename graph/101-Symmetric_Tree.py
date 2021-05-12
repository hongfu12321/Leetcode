'''
G-101-Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

 
But the following `[1,2,2,null,3,null,3]` is not:

        1
       / \
      2   2
       \   \
       3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric_recursion(self, root: TreeNode) -> bool:
            def helper(one, two):
                if not one and not two: return True
                if not one or not two: return False
                if one.val != two.val: return False          
                return helper(one.left, two.right) and helper(one.right, two.left)
            
            return helper(root.left, root.right) if root else True

    
def isSymmetric_bfs(self, root):
        if not root: return True
        queue = [root.left, root.right]
        
        while len(queue) > 0:
            # pop 2 from queue
            left = queue.pop(0)
            right = queue.pop(0)
            
            # Evalate the pair
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                pass
            else:
                return False
            
            # Enqueue children
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True

    
def isSymmetric_dfs(self, root: TreeNode) -> bool:
        inorderNodeList = []
        postorderNodeList = []
        
        left = right = root
        while left or inorderNodeList:
            while left and right:
                inorderNodeList.append(left)
                postorderNodeList.append(right)
                left = left.left
                right = right.right
            if left or right: return False
            left = inorderNodeList.pop()
            right = postorderNodeList.pop()           
            if left.val != right.val: return False
            
            left = left.right
            right = right.left
            
        return True