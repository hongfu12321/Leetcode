# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []        
        while head:
            res.append(head.val)
            head = head.next
            
        return res == res[::-1]

'''
Runtime: 820 ms, faster than 52.30% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.8 MB, less than 62.41% of Python3 online submissions for Palindrome Linked List.
'''