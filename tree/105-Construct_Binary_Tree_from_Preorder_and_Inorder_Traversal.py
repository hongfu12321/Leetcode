# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
'''
def preorder(root):
    if not root: return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root: return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
       
        root.left = self.buildTree(preorder[1:root_index + 1],inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:],inorder[root_index + 1:])
        
        return root

'''
Runtime: 200 ms, faster than 23.04% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.4 MB, less than 20.66% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''