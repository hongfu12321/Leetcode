# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return        
        
        def helper(left, right):
            if left >= right: return 
            if right - left == 1: return TreeNode(nums[left])
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            node.left = helper(left, mid)
            node.right = helper(mid + 1, right)
            return node
        
        return helper(0, len(nums))

'''
Runtime: 52 ms, faster than 95.58% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 59.79% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''