# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0: return head

        slow = fast = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head

'''
Runtime: 28 ms, faster than 92.29% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.2 MB, less than 49.36% of Python3 online submissions for Remove Nth Node From End of List.
'''
