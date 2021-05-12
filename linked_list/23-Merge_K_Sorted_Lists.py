'''
LL-23-Merge k Sorted Lists

Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6
'''


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2: return l1 or l2        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
       
    
    def mergeKLists_mergeSort(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        middle = length // 2
        
        if not lists: return None
        if length == 1: return lists[0]
        
        tmp1 = self.mergeKLists(lists[:middle])
        tmp2 = self.mergeKLists(lists[middle:])
        
        return self.mergeTwoLists(tmp1, tmp2) 

    

    def mergeKLists_fast(self, lists: List[ListNode]) -> ListNode:
            values = []        
            for list in lists:
                while list:
                    values.append(list.val)
                    list = list.next
            
            head = tail = ListNode(0)
            for val in sorted(values):
                tail.next = ListNode(val)
                tail = tail.next
            
            return head.next