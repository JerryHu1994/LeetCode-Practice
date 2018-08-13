class Solution(object):
    def dfs(self, matrix,dp, y, x, prev):
        if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix) or dp[y][x] or matrix[y][x] < prev:
            return
        dp[y][x] = True
        self.dfs(matrix, dp, y-1, x, matrix[y][x])
        self.dfs(matrix, dp,y, x-1, matrix[y][x])
        self.dfs(matrix, dp,y+1, x, matrix[y][x])
        self.dfs(matrix, dp,y, x+1, matrix[y][x])
    
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0: return []
        height, width = len(matrix), len(matrix[0])
        dp_pac = [[False]*width for i in range(height)]
        dp_alt = [[False]*width for i in range(height)]
        
        # first and last row
        for i in range(width):
            self.dfs(matrix, dp_pac, 0, i, float("-inf"))
            self.dfs(matrix, dp_alt, height-1, i, float("-inf"))
        
        # first and last col
        for i in range(height):
            self.dfs(matrix, dp_pac, i, 0, float("-inf"))
            self.dfs(matrix, dp_alt, i, width-1, float("-inf"))
            
        # count double true
        ret = []
        for i in range(height):
            for j in range(width):
                if dp_pac[i][j] and dp_alt[i][j]:
                    ret.append([i, j])
        return ret
        
                