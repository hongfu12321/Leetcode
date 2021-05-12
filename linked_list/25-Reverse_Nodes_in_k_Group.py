'''

Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
Example:
Given this linked list: `1->2->3->4->5`
For k = 2, you should return: `2->1->4->3->5`
For k = 3, you should return: `3->2->1->4->5`
Note:

- Only constant extra memory is allowed.
- You may not alter the values in the list's nodes, only nodes itself may be changed.

'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
                        
                                
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
                
        # After reverse, we know that `head` is the tail of the group.
                # And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev