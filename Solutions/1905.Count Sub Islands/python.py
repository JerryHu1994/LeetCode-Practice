class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        ans = 0
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return True
            if grid2[row][col] != 1:
                return True
            grid2[row][col] = 0
            top = dfs(row - 1, col)
            bot = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            
            if grid1[row][col] != 1:
                return False
            return top and bot and left and right
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)
        return ans