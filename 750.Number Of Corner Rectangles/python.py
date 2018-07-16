class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h, w = len(grid), len(grid[0])
        ret = 0
        for i in range(h):
            for j in range(i+1, h):
                curr = 0
                for k in range(w):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        curr += 1
                ret += curr*(curr-1)/2
        return ret