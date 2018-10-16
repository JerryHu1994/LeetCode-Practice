class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:    return 0
        height, width = len(grid), len(grid[0])
        ret = 0
        cntmap = [[0]*width for i in range(height)]
        enemies = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "E":   enemies.append((i,j))
        for e in enemies:
            ey, ex = e
            # left 
            left = ex-1
            while left >=0 and grid[ey][left] != 'W':
                if grid[ey][left] == '0':
                    cntmap[ey][left] += 1
                    ret = max(ret, cntmap[ey][left])
                left -= 1
            # right 
            right = ex+1
            while right < width and grid[ey][right] != 'W':
                if grid[ey][right] == '0':
                    cntmap[ey][right] += 1
                    ret = max(ret, cntmap[ey][right])
                right += 1
            # up 
            up = ey-1
            while up >= 0 and grid[up][ex] != 'W':
                if grid[up][ex] == '0':
                    cntmap[up][ex] += 1
                    ret = max(ret, cntmap[up][ex])
                up -= 1
            # down 
            down = ey+1
            while down < height and grid[down][ex] != 'W':
                if grid[down][ex] == '0':
                    cntmap[down][ex] += 1
                    ret = max(ret, cntmap[down][ex])
                down += 1
        return ret