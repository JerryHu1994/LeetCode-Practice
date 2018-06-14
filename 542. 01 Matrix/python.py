class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        ret = [[m*n]*n for i in range(m)]
        # top to bottom
        for i in range(m):
            # left to right
            for j in range(n):
                if matrix[i][j] == 0:   ret[i][j] = 0
                if j > 0:
                    ret[i][j] = min(ret[i][j], ret[i][j-1]+1)
                if i > 0:
                    ret[i][j] = min(ret[i][j], ret[i-1][j]+1)
        # bottom to up
        for i in range(m-1, -1, -1):
            # right to left
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0:   ret[i][j] = 0
                if j < n-1:
                    ret[i][j] = min(ret[i][j], ret[i][j+1]+1)
                if i < m-1:
                    ret[i][j] = min(ret[i][j], ret[i+1][j]+1)
        return ret
                
            
                    
            