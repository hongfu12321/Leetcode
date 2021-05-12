'''
BT-100-Same Tree

Easy

Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

'''


class Solution:
    def isSameTree_recursion(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and \
                self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    
    def isSameTree_iterate(self, p: TreeNode, q: TreeNode) -> bool:
            nodep = []
            nodeq = []
            
            while p or q or nodep or nodeq:
                while p and q:
                    nodep.append(p)
                    nodeq.append(q)
                    p = p.left
                    q = q.left            
                if p != q: return False
                
                p = nodep.pop()
                q = nodeq.pop()
                if p.val != q.val: return False
                
                p = p.right
                q = q.right
                    
            return True    