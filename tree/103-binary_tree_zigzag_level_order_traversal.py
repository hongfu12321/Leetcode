# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. help function pass level in to decide the printing direction
2. level begin at 0, if [level % 2 == 0 : left -> right]

'''


class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return [] 
#         res = []       
        
#         def helper(node: ListNode, level: int):
#             if not node: return
#             if len(res) == level: res.append([])
            
#             res[level].append(node.val)
#             helper(node.left, level + 1)
#             helper(node.right, level + 1)
        
#         helper(root, 0)
        
#         return [lst if i % 2 == 0 else lst[::-1] for i, lst in enumerate(res)]

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, stack, q = [], [], collections.deque([])
        
        curr_level = 0
        
        def helper(node, level):
            print(level, curr_level)
            if level > curr_level:
                res.append([])
                if curr_level % 2 == 0:
                    while q:
                        res[curr_level].append(q.popleft)
                else:
                    while stack:
                        res[curr_level].append(stack.pop)
                curr_level += 1        
                
                
            if level % 2 == 0:
                q.append(node)
            else:
                stack.append(node)
        
        helper(root, 0)
        return res