class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def checkIsland(j, i):
            if grid[j][i] == '1':
                grid[j][i] = '0'
                if j + 1 < row: checkIsland(j + 1, i)
                if j - 1 >= 0:  checkIsland(j - 1, i)
                if i - 1 >= 0:  checkIsland(j, i - 1)
                if i + 1 < col: checkIsland(j, i + 1)
            
        row, col = len(grid), len(grid[0])
        count = 0
        for j in range(row):
            for i in range(col):
                if grid[j][i] == "1":
                    count += 1
                    checkIsland(j, i)
                    
        return count

'''
Runtime: 128 ms, faster than 94.29% of Python3 online submissions for Number of Islands.
Memory Usage: 15.6 MB, less than 27.70% of Python3 online submissions for Number of Islands.
'''