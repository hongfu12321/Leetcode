# Given a binary tree, return the inorder traversal of its nodes' values.
'''
Depth First Traversals:
(a) In-order (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
'''

class Solution:
    def inorderTraversal_recursion(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right:
            return [root.val]
        
        return self.inorderTraversal(root.left) + [root.val] + \
                self.inorderTraversal(root.right)
    

    def inorderTraversal_iterate(self, root: TreeNode) -> List[int]:
            lst = []
            nodeLst = []
            node = root
            while node or nodeLst:
                while node:
                    nodeLst.append(node)
                    node = node.left
                node = nodeLst.pop()
                lst.append(node.val)
                node = node.right
            return lst
