# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right: return head
        
        curr = head
        dummy = pre = ListNode(-1, head)        
        for _ in range(left - 1):
            pre = curr
            curr = curr.next
        
        lst_begin, lst_end = pre, curr
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        lst_begin.next = pre
        lst_end.next = curr
        
        return dummy.next

'''
Runtime: 28 ms, faster than 83.07% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 14.1 MB, less than 97.57% of Python3 online submissions for Reverse Linked List II.
'''