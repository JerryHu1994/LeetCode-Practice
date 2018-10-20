class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        dic = {} # group id to size
        # construct groups and mapping
        height, width = len(grid), len(grid[0])
        visited = set()
        groupidx = 2
        # no zero
        if sum([sum(i) for i in grid]) == height*width: return height*width
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cnt, queue = 0, [(i,j)]
                    visited.add((i,j))
                    while queue:
                        curry, currx = queue.pop(0)
                        cnt += 1
                        grid[curry][currx] = groupidx
                        if curry > 0 and grid[curry-1][currx] == 1 and (curry-1, currx) not in visited:
                            queue.append((curry-1, currx))
                            visited.add((curry-1, currx))
                        if curry < height-1 and grid[curry+1][currx] == 1 and (curry+1, currx) not in visited:
                            queue.append((curry+1, currx))
                            visited.add((curry+1, currx))
                        if currx > 0 and grid[curry][currx-1] == 1 and (curry, currx-1) not in visited:
                            queue.append((curry, currx-1))
                            visited.add((curry, currx-1))
                        if currx < width-1 and grid[curry][currx+1] == 1 and (curry, currx+1) not in visited:
                            queue.append((curry, currx+1))
                            visited.add((curry, currx+1))
                    dic[groupidx] = cnt
                    groupidx += 1
        # inspect each 0
        ret = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    curry, currx = y, x
                    neighbors = set()
                    if curry > 0 and grid[curry-1][currx] != 0:   neighbors.add(grid[curry-1][currx])
                    if curry < height-1 and grid[curry+1][currx] != 0:   neighbors.add(grid[curry+1][currx])
                    if currx > 0 and grid[curry][currx-1] != 0:   neighbors.add(grid[curry][currx-1])
                    if currx < width-1 and grid[curry][currx+1] != 0:   neighbors.add(grid[curry][currx+1])
                    ret = max(ret, 1+sum([dic[i] for i in neighbors]))
        
        return ret
                    