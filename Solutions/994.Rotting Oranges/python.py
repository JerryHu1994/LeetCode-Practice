class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        queue = []
        freshcnt = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshcnt += 1
        visited = set(queue)
        ans, currcnt = 0, 0
        while len(queue) and currcnt < freshcnt:
            currsize = len(queue)
            for i in range(currsize):
                currx, curry = queue.pop(0)
                for nexty, nextx in [(currx-1, curry), (currx, curry-1), (currx+1, curry), (currx, curry+1)]:
                    if 0 <= nexty < height and 0 <= nextx < width and (nexty, nextx) not in visited and grid[nexty][nextx] == 1:
                        visited.add((nexty, nextx))
                        queue.append((nexty, nextx))
                        currcnt += 1
            ans += 1
        return ans if currcnt == freshcnt else -1