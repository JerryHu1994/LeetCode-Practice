class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        leftright = [max(i) for i in grid]
        topbottom = [max(i) for i in zip(*grid)]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(leftright[i], topbottom[j]) - grid[i][j]
        return ret