'''
545. Boundary of Binary Tree

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.
Given the root of a binary tree, return the values of its boundary.

Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''
    For left bound
    1. check if there if left leaf or right leaf, if node have one of them, append val to res
    2. if there is left leaf, move to left. Or move to right
    
    For right bound
    1. Similar to left bound
    
    For end bound
    1. dfs to the end, if node has no child, append to res
    
    res append order: left -> end -> root -> end -> right
    '''
    
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        def getLeftBound(node):
            if node and (node.left or node.right):
                res.append(node.val)
            if node.left:
                getLeftBound(node.left)
            elif node.right:
                getLeftBound(node.right)
            
        def getRightBound(node):
            if node.right:
                getRightBound(node.right)
            elif node.left:
                getRightBound(node.left)
            if node and (node.left or node.right):
                res.append(node.val)
        
        def getEndBound(node):
            if node.left:
                getEndBound(node.left)
            if node.right:
                getEndBound(node.right)
            if not node.left and not node.right:
                res.append(node.val)
        
        res = []
        
        if root:
            res.append(root.val)
            if root.left:
                getLeftBound(root.left)
                getEndBound(root.left)
            if root.right:
                getEndBound(root.right)
                getRightBound(root.right)
                
        return res
    
    '''
    Runtime: 44 ms, faster than 78.62% of Python3 online submissions for Boundary of Binary Tree.
    Memory Usage: 16.5 MB, less than 38.69% of Python3 online submissions for Boundary of Binary Tree.
    '''