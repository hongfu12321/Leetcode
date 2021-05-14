'''
1448. Count Good Nodes in Binary Tree
Medium

Given a binary tree root, a node X in the tree is named good 
if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0
        
        def dfs(node, max_num):
            if not node: return
           
            nonlocal good_node
            if node.val >= max_num:
                good_node += 1
                max_num = node.val
            dfs(node.left, max_num)
            dfs(node.right, max_num)
            
        dfs(root, root.val)
        
        return good_node
        
'''
Runtime: 220 ms, faster than 98.68% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 33.5 MB, less than 41.32% of Python3 online submissions for Count Good Nodes in Binary Tree.
'''