class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mid = n/2
        # flip vertically
        for i in range(0, n):
            for j in range(0, mid):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
        # flip via diagonal
        for i in range(0, n):
            for j in range(0, n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
            
                
        
                
        