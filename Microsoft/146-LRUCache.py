from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)





# class ListNode:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.head = ListNode(1, 1)
#         self.tail = ListNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.cache = {}

#     # if key in dic, move node from list, then insert into front, return val
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self.removeFromList(node)
#         self.insertToHead(node)
#         return node.val        

#     # if key in dic, update val, then move to the front
#     # else: if reach capacity, remove the least node, del key in cache
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.val = value
#             self.removeFromList(node)
#             self.insertToHead(node)
#         else:
#             if len(self.cache) == self.capacity:
#                 self.removeLeastNode()
#             new_node = ListNode(key, value)
#             self.insertToHead(new_node)
#             self.cache[key] = new_node
    
#     def insertToHead(self, node):
#         head_node = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = head_node
#         head_node.prev = node
    
#     def removeFromList(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
        
#     def removeLeastNode(self):
#         least = self.tail.prev
#         self.removeFromList(least)
#         del self.cache[least.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)