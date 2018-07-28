class Solution(object):
    
    def dfs(self, grid, x, y, di):
        if x>=0 and x<len(grid[0]) and y>=0 and y<len(grid) and not self.visited[y][x] and grid[y][x]:
            self.currShape += di
            self.visited[y][x] = True
            self.dfs(grid, x+1, y, "1")
            self.dfs(grid, x-1, y, "2")
            self.dfs(grid, x, y+1, "3")
            self.dfs(grid, x, y-1, "4")
            self.currShape += "0"
        
    
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0: return 0
        height, width = len(grid), len(grid[0])
        self.s = set()
        self.visited = [[False]*width for i in range(height)]
        self.currShape = ""
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    self.currShape = ""
                    self.dfs(grid, j, i, "0")
                    if len(self.currShape): self.s.add(self.currShape)
        return len(self.s)
                    