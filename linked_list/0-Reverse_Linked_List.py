
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
      self.val = x
      self.next = None
  
class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_unit(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        nxt = curr.next
        curr.next = prev
        self.reverse_unit(nxt, curr)

    def reverse_r(self):
        if self.head is None: return 
        self.reverse_unit(self.head, None)

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next