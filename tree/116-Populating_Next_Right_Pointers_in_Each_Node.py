class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return 
        q = collections.deque([root])
        dummy = root
        while q:
            pre, q_len = None, len(q)
            for i in range(q_len):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                if pre:
                    pre.next = node
                    if i == q_len - 1:
                        node.next = None
                pre = node
                
        return root
    

#     def connect(self, root: 'Node') -> 'Node':    
#         node = root
        
#         while node:
#             if node.left:
#                 nextLevel = node.left
#             else: 
#                 break
            
#             while node:
#                 node.left.next = node.right
#                 pre = node.right
#                 if node.next:
#                     node = node.next
#                     pre.next = node.left
#                 else:
#                     node = nextLevel
#                     break
                    
#         return root
