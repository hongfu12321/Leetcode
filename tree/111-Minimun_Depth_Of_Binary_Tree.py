# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = collections.deque([root])
        
        depth = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if not node.left and not node.right: return depth
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            depth += 1
            
        return 0

'''
Runtime: 464 ms, faster than 95.74% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.2 MB, less than 80.32% of Python3 online submissions for Minimum Depth of Binary Tree.
'''