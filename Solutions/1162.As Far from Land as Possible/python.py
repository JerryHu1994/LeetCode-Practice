class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        dismap = [[101]*width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    visited = set()
                    queue = [(i, j, 0)]
                    visited.add((i,j))
                    while len(queue):
                        y, x, level = queue.pop(0)
                        if grid[y][x] == 0:
                            dismap[y][x] = min(dismap[y][x], level)
                        if y > 0 and grid[y-1][x] == 0 and (y-1, x) not in visited:
                            if dismap[y-1][x] > level+1:
                                queue.append((y-1, x, level+1))
                                visited.add((y-1, x))
                        if y < height-1 and grid[y+1][x] == 0 and (y+1, x) not in visited:
                            if dismap[y+1][x] > level+1:
                                queue.append((y+1, x, level+1))
                                visited.add((y+1, x))
                        if x > 0 and grid[y][x-1] == 0 and (y, x-1) not in visited:
                            if dismap[y][x-1] > level+1:
                                queue.append((y, x-1, level+1))
                                visited.add((y, x-1))
                        if x < width-1 and grid[y][x+1] == 0 and (y, x+1) not in visited:
                            if dismap[y][x+1] > level+1:
                                queue.append((y, x+1, level+1))
                                visited.add((y, x+1))
        ans = -1
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    ans = max(dismap[i][j], ans)
        return ans if ans != 101 else -1
                
        