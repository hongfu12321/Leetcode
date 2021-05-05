# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # We can also use fast, slow points to find the middle node
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        def helper(l, r):
            # boundary
            if l >= r: return 
            if r - l == 1: return TreeNode(arr[l])
            
            # mid
            mid = (l + r) // 2
            node = TreeNode(arr[mid])
    
            # left
            node.left = helper(l, mid)
        
            # right
            node.right = helper(mid + 1, r)
            
            return node
            
        return helper(0, len(arr))
            
'''
Runtime: 120 ms, faster than 95.03% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 20.5 MB, less than 32.00% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
'''