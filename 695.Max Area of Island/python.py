class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width, height = len(grid[0]), len(grid)
        visited = [[False]*width for i in range(height)]
        ret = 0
        for i in range(height):
            for j in range(width):
                if not visited[i][j] and grid[i][j] == 1:
                    # do search
                    area = 0
                    queue = [(i, j)]
                    visited[i][j] = True
                    while len(queue):
                        curri, currj = queue.pop(0)
                        area += 1
                        # top
                        if curri-1>=0 and not visited[curri-1][currj] and grid[curri-1][currj] == 1:
                            visited[curri-1][currj] = True
                            queue.append((curri-1,currj))
                        # right
                        if currj+1<width and not visited[curri][currj+1] and grid[curri][currj+1] == 1:
                            visited[curri][currj+1] = True
                            queue.append((curri, currj+1))
                        # down
                        if curri+1 < height and not visited[curri+1][currj] and grid[curri+1][currj] == 1:
                            visited[curri+1][currj] = True
                            queue.append((curri+1, currj))
                        # left
                        if currj-1 >=0 and not visited[curri][currj-1] and grid[curri][currj-1] == 1:
                            visited[curri][currj-1] = True
                            queue.append((curri, currj-1))
                    ret = max(ret, area)
        return ret