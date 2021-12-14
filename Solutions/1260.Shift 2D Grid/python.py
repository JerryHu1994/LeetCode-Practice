class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for i in range(m)]
        def computefinalcoord(y, x, k):
            for i in range(k):
                if y == m-1 and x == n-1:
                    y, x = 0, 0
                elif x == n-1:
                    y, x = y+1, 0
                else:
                    x = x+1
            return (y, x)
        for y in range(m):
            for x in range(n):
                val = grid[y][x]
                finaly, finalx = computefinalcoord(y, x, k)
                ans[finaly][finalx] = val
        return ans