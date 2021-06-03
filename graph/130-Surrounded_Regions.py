'''
130. Surrounded Regions
Medium

Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_row, max_col = len(board), len(board[0])
        
        def valid_node(row, col):
            return row >= 0 and row < max_row and col >= 0 and col < max_col
        
        def dfs(row, col):
            if not valid_node(row, col): return
            
            if board[row][col] == 'O':
                board[row][col] = '1'
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        # stupid way to find the boarder
        corner = []
        corner.extend([[0, k] for k in range(max_col)])
        corner.extend([[max_row - 1, k] for k in range(max_col)])
        corner.extend([k, 0] for k in range(1, max_row - 1))
        corner.extend([k, max_col - 1] for k in range(1, max_row - 1))
        
        for [i, j] in corner:
            if board[i][j] == 'O': dfs(i, j)
        
        for row in range(max_row):
            for col in range(max_col):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '1':
                    board[row][col] = 'O'
        
        return board
    