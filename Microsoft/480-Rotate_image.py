'''
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        [0, 0] -> [0, 2]; [0, 1], [1, 2]
            -> up and right:    up[0, 0->x-1], right[0->x-1, x]
            -> right, down:     right[0->x-1, x], down[x, x->1]
            -> down, left:      down[x, x->1], left[x->1, 0]
            -> left, up:        left[x->1, 0], up[0, 0->x-1]
        
        '''
        
        def rotate_boundary(start, length):
            if length == 0: return
            y, x = start[0], start[1]
            
            for l in range(length):
                up = matrix[y][x + l]
                right = matrix[y + l][x + length]
                down = matrix[y + length][x + length - l]
                left = matrix[y + length - l][x]
                
                matrix[y][x + l] = left
                matrix[y + l][x + length] = up
                matrix[y + length][x + length - l] = right
                matrix[y + length - l][x] = down

        
        length = len(matrix) - 1
        start = [0, 0]
        while length > 0:
            rotate_boundary(start, length)
            length -= 2
            start[0] += 1
            start[1] += 1
            