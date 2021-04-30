# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = tmp = 0
        head = result = ListNode()
        
        while l1 and l2:
            carry, tmp = divmod(l1.val + l2.val + carry, 10)
            result.next = ListNode(tmp)
            result = result.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            carry, tmp = divmod(l1.val + carry, 10)
            result.next = ListNode(tmp)
            result = result.next
            l1 = l1.next
            
        while l2:
            carry, tmp = divmod(l2.val + carry, 10)
            result.next = ListNode(tmp)
            result = result.next
            l2 = l2.next
        
        if carry:
            result.next = ListNode(carry)
        
        return head.next

'''
Runtime: 64 ms, faster than 87.86% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.4 MB, less than 12.16% of Python3 online submissions for Add Two Numbers.
'''