'''
118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            cur_level = [1]
            pre_level = res[-1]
            for j in range(i - 1):
                cur_level.append(pre_level[j] + pre_level[j + 1])
            cur_level.append(1)
            res.append(cur_level)
            
        return res
    
'''
Runtime: 28 ms, faster than 81.66% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14.3 MB, less than 55.80% of Python3 online submissions for Pascal's Triangle.
'''

