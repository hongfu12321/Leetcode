class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
    # keep right -> down -> left -> up, until met the end
    # append node in to result array
    # update the boundary when we finished one direction
    
        if len(matrix) < 1: return []

        res = []
        boundary = [left_bound, right_bound, up_bound, down_bound] = [0, len(matrix[0]), 0, len(matrix)]

        while left_bound < right_bound and up_bound < down_bound:
            # right
            for i in range(left_bound, right_bound):
                res.append(matrix[up_bound][i])
                
            # down
            for i in range(up_bound + 1, down_bound):
                res.append(matrix[i][right_bound - 1])
            
            if right_bound - left_bound > 1 and down_bound - up_bound > 1:
                # left
                for i in reversed(range(left_bound, right_bound - 1)):
                    res.append(matrix[down_bound - 1][i])

                # up
                for i in reversed(range(up_bound + 1, down_bound - 1)):
                    res.append(matrix[i][left_bound])
            
            left_bound += 1
            right_bound -= 1
            up_bound += 1
            down_bound -= 1

        return res

'''
Runtime: 20 ms, faster than 99.04% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14 MB, less than 94.36% of Python3 online submissions for Spiral Matrix.
'''
    
    
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         def spiral_coor(r1, r2, c1, c2):
#             for c in range(c1, c2 + 1):
#                 yield r1, c
#             for r in range(r1 + 1, r2 + 1):
#                 yield r, c2
                
#             if r1 < r2 and c1 < c2:
#                 for c in reversed(range(c1, c2)):
#                     yield r2, c
#                 for r in reversed(range(r1 + 1, r2)):
#                     yield r, c1
                    
#         if not matrix: return []
#         ans = []
#         r1, r2 = 0, len(matrix) - 1
#         c1, c2 = 0, len(matrix[0]) - 1
        
#         while r1 <= r2 and c1 <= c2:
#             for r, c in spiral_coor(r1, r2, c1, c2):
#                 ans.append(matrix[r][c])
#             r1 += 1; r2 -= 1
#             c1 += 1; c2 -= 1
#         return ans
# '''
# Runtime: 28 ms, faster than 84.80% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14 MB, less than 99.07% of Python3 online submissions for Spiral Matrix.
# '''
            
            
            