class Solution(object):
    
    def dfs(self, matrix, path, y, x):
        if path[y][x] != None:
            return path[y][x]
        if (x==0 or matrix[y][x] >= matrix[y][x-1]) and (x==len(matrix[0])-1 or matrix[y][x] >= matrix[y][x+1]) and (y==0 or matrix[y][x] >= matrix[y-1][x]) and (y==len(matrix)-1 or matrix[y][x] >= matrix[y+1][x]):
            path[y][x] = 1
            self.ret = max(self.ret, 1)
            return 1
        
        curr = matrix[y][x]
        ret = 1
        # up
        if y>0 and curr < matrix[y-1][x]:
            if path[y-1][x] != None:
                ret = max(ret, path[y-1][x]+1)
            else:
                ret = max(ret, self.dfs(matrix, path, y-1, x)+1)
        # left 
        if x>0 and curr < matrix[y][x-1]:
            if path[y][x-1] != None:
                ret = max(ret, path[y][x-1]+1)
            else:
                ret = max(ret, self.dfs(matrix, path, y, x-1)+1)
        # down
        if y<len(matrix)-1 and curr < matrix[y+1][x]:
            if path[y+1][x] != None:
                ret = max(ret, path[y+1][x]+1)
            else:
                ret = max(ret, self.dfs(matrix, path, y+1, x)+1)
        # right
        if x<len(matrix[0])-1 and curr < matrix[y][x+1]:
            if path[y][x+1] != None:
                ret = max(ret, path[y][x+1]+1)
            else:
                ret = max(ret, self.dfs(matrix, path, y, x+1)+1)
        path[y][x] = ret
        self.ret = max(self.ret, ret)
        return ret
            
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0: return 0
        height, width = len(matrix), len(matrix[0])
        self.ret = 0
        path = [[None]*width for i in range(height)]
        for i in range(height):
            for j in range(width):
                self.dfs(matrix, path, i, j)
        return self.ret