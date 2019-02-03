class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        nums = sum([grid[i][j] == 1 for i in range(height) for j in range(width)])
        dis_count, visit_count = [[0]*width for i in range(height)], [[0]*width for i in range(height)]
        def bfs(y, x):
            currdis = 0
            queue = [(y, x)]
            visited = set()
            visited.add((y, x))
            while len(queue):
                qlen = len(queue)
                for i in range(qlen):
                    curry, currx = queue.pop(0)
                    visit_count[curry][currx] += 1
                    dis_count[curry][currx] += currdis
                    for nexty, nextx in [(curry+1, currx), (curry-1, currx), (curry, currx+1), (curry, currx-1)]:
                        if 0 <= nexty < height and 0 <= nextx < width and grid[nexty][nextx] == 0 and (nexty, nextx) not in visited:
                            queue.append((nexty, nextx))
                            visited.add((nexty, nextx))
                currdis += 1
                
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1: bfs(i, j)
        candidates = [dis_count[i][j]  for i in range(height) for j in range(width) if grid[i][j] == 0 and visit_count[i][j] == nums]
        if len(candidates) == 0:
            return -1
        else:
            return min(candidates)