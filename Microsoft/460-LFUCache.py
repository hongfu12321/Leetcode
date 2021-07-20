class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.cnt = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.key2node = {}
        self.cnt2node = collections.defaultdict(collections.OrderedDict)
        

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        del self.cnt2node[node.cnt][key]
        
        if not self.cnt2node[node.cnt]:
            del self.cnt2node[node.cnt]
            
        node.cnt += 1
        self.cnt2node[node.cnt][key] = node
        
        if self.minFreq not in self.cnt2node:
            self.minFreq += 1
        
        return node.val
        
    # if not capacity, return
    # if key in key2node, update value, update list
    # else: if reach capacity, remove the least node in self.minfreq
    # create new node, add it into cnt2node[1], minFreq = 1
    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return 
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
            return
        
        if self.capacity == len(self.key2node):
            k, v = self.cnt2node[self.minFreq].popitem(last=False)
            del self.key2node[k]
        
        self.key2node[key] = self.cnt2node[1][key] = Node(key, value)
        self.minFreq = 1
        return



# class ListNode: 
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.freq = 1
#         self.prev = None
#         self.next = None

        
# '''
# 1. func: insertIntoHead
# 2. func: removeFromList
# 3. func: removeLeastNode

# '''
# class DLL:
#     def __init__(self):
#         self.head = ListNode(1, 1)
#         self.tail = ListNode(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.size = 0
        
#     def insertIntoHead(self, node):
#         head_node = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = head_node
#         head_node.prev = node
#         self.size += 1
        
#     def removeFromList(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         self.size -= 1
        
#     def removeLeastNode(self):
#         least = self.tail.prev
#         self.removeFromList(least)
#         return least

# '''
# 1. need freqTable to store DLL which every node has same freq
# 2. need cache to store node for the key

# '''        
# class LFUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.minFreq = 0
#         self.cache = {}
#         self.freqTable = collections.defaultdict(DLL)
        
#     def print_freqTable(self):
#         for key in self.freqTable:
#             print(key, end=" | ")
#             node = self.freqTable[key].head
#             while node.next:
#                 print(node.key, end="->")
#                 node = node.next
#             print(node.key)
#         print("-------------------------")

#     # If the key in dic, delete node in freqTable, update freq then add node into new position of freqTable
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1   
#         node = self.cache[key]
#         self.updateNode(key, node.val)
#         return node.val
        
#     # If the key in dic, delete node in freqTable, update freq then add node into new position of freqTable
#     # Else, if reach capacity, remove least node from freqTable[minFreq]. Then add new node in freqTable[1]
#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0: 
#             return 
#         if key in self.cache:
#             self.updateNode(key, value)
#         else:
#             if self.capacity == len(self.cache):
#                 least = self.freqTable[self.minFreq].removeLeastNode()
#                 del self.cache[least.key]
#             node = ListNode(key, value)
#             self.freqTable[1].insertIntoHead(node)
#             self.cache[key] = node
#             self.minFreq = 1
    
    
#     def updateNode(self, key, val):
#         node = self.cache[key]
#         node.val = val
#         prev_freq = node.freq
#         node.freq += 1
#         self.freqTable[prev_freq].removeFromList(node)
#         self.freqTable[node.freq].insertIntoHead(node)
        
#         if self.minFreq == prev_freq and self.freqTable[prev_freq].size == 0:
#             self.minFreq += 1
    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)