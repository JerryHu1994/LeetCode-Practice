class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        self.ans = 0
        starty, startx = None, None
        endy, endx = None, None
        empty_cnt = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1:   empty_cnt += 1
                if val == 1:    starty, startx = r, c
                if val == 2:    endy, endx = r, c
        def dfs(y, x, currcnt):
            currcnt -= 1
            if currcnt < 0: return
            if y == endy and x == endx:
                if currcnt == 0:    self.ans += 1
                return
            grid[y][x] = -1
            for diry, dirx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nexty, nextx = y+diry, x+dirx
                if 0 <= nexty < height and 0 <= nextx < width and grid[nexty][nextx] != -1:
                    dfs(nexty, nextx, currcnt)
            grid[y][x] = 0
        dfs(starty, startx, empty_cnt)
        return self.ans