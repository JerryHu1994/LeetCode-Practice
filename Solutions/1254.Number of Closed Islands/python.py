class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        visited = set()
        self.ans = 0
        def dfs(starty, startx):
            queue = [(starty, startx)]
            isclosed = True
            while len(queue):
                y, x = queue.pop(0)
                if y == 0 or y == height-1 or x == 0 or x == width-1:
                    isclosed = False
                if y > 0 and (y-1, x) not in visited and grid[y-1][x] == 0:
                    queue.append((y-1, x))
                    visited.add((y-1, x))
                if y < height-1 and (y+1, x) not in visited and grid[y+1][x] == 0:
                    queue.append((y+1, x))
                    visited.add((y+1, x))
                if x > 0 and (y, x-1) not in visited and grid[y][x-1] == 0:
                    queue.append((y, x-1))
                    visited.add((y, x-1))
                if x < width-1 and (y, x+1) not in visited and grid[y][x+1] == 0:
                    queue.append((y, x+1))
                    visited.add((y, x+1))
            if isclosed:    self.ans += 1
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    if (i, j) not in visited:
                        dfs(i, j)
        return self.ans