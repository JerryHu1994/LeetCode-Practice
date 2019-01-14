class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(pts):
            ans = 0
            l, r = 0, len(pts)-1
            while l < r:
                ans += pts[r] - pts[l]
                l += 1
                r -= 1
            return ans
        height, width = len(grid), len(grid[0])
        pts = [(i, j)   for i in range(height)  for j in range(width) if grid[i][j] == 1]
        sorted_y, sorted_x = sorted([p[0] for p in pts]), sorted([p[1] for p in pts])
        return helper(sorted_y)+helper(sorted_x)