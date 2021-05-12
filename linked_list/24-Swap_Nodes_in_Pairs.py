'''
LL-24-Swap Nodes in Pairs

Medium

Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
 
Example:

    Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

class Solution:
    def swapPairs_loop(self, head: ListNode) -> ListNode:
        carry = 0
        
        if not head or not head.next: return head
        
        tail = dummy = ListNode()
        dummy.next = head
        carry = 0
        while head:
            if carry == 0:
                carry = 1
                firstNode = head
            else:
                carry = 0
                tail.next = head
                first.next = head.next
                head.next = firstNode
                tail = firstNode
            head = firstNode.next

        return dummy.next

        
    def swapPairs_recursion(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        firstNode = head.next
        secondNode = head
        
        secondNode.next = self.swapPairs(head.next.next)        
        firstNode.next = secondNode
        
        return firstNode