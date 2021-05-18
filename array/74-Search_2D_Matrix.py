'''
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
        
#         # search from left of first row
#         for row in range(0, m):
#             if target == matrix[row][n - 1]:
#                 return True
#             if target < matrix[row][n - 1]:
#                 for col in range(0, n):
#                     if target == matrix[row][col]:
#                         return True
#                 return False
            
#         return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (high + low) // 2
            mid_val = matrix[mid // n][mid % n]
            
            
            if mid_val == target:
                return True
            elif mid_val > target: high = mid - 1
            elif mid_val < target: low = mid + 1
                
        return False

'''
Runtime: 40 ms, faster than 82.32% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.8 MB, less than 30.49% of Python3 online submissions for Search a 2D Matrix.
'''