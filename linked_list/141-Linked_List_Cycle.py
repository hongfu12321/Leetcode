# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

'''
Runtime: 52 ms, faster than 77.22% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.6 MB, less than 75.61% of Python3 online submissions for Linked List Cycle.
'''