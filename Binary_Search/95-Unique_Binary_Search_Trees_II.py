'''
Given an integer `n`, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
Example:

    Input: 3
    Output:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    Explanation:
    The above output corresponds to the 5 unique BST's shown below:
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(lower: int, upper:int):
            if lower > upper:
                return [None]
            
            ret = []
            for root in range(lower, upper + 1):
                for left in helper(lower, root - 1):
                    for right in helper(root + 1, upper):
                        ret.append(TreeNode(root, left, right))
            return ret    
        return helper(1, n) if n > 0 else []