class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_area = 6*sum([sum(i) for i in grid])
        # remove horizontally overlapped faces
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 1:
                    total_area -= (grid[i][j] - 1)*2
        # remove vertically overlapped faces
        for i in range(len(grid)):
            for j in range(len(grid[i])-1):
                total_area -= (min(grid[i][j], grid[i][j+1]))*2
        trans = zip(*grid)
        for i in range(len(trans)):
            for j in range(len(trans[i])-1):
                total_area -= (min(trans[i][j], trans[i][j+1]))*2
        return total_area