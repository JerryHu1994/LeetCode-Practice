class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        ret = 0
        # check four borders
        for i in range(height):
            if grid[i][0] == 1: ret += 1
            if grid[i][width-1] == 1:   ret += 1
        for i in range(width):
            if grid[0][i] == 1: ret += 1
            if grid[height-1][i] == 1:   ret += 1
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    if j<width-1 and grid[i][j+1]==1: ret += 1
                    if j>0 and grid[i][j-1]==1:   ret += 1
                    if i>0 and grid[i-1][j]==1: ret += 1
                    if i<height-1 and grid[i+1][j]==1:  ret += 1
        return ret
        