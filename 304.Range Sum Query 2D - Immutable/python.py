class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.height = len(matrix)
        self.width = len(matrix[0]) if self.height!=0 else 0
        self.dp = [[None]*self.width for i in range(self.height)]
        self.matrix = matrix

    # return sum from (0,0) to (row, col)
    def getSum(self, row, col):
        ret = 0
        for i in range(row+1):
            ret += sum(self.matrix[i][0:col+1])
        return ret
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.height == 0:    return 0
        if row1 > 0 and col1 > 0:
            if self.dp[row1-1][col1-1] == None:
                topleft = self.getSum(row1-1, col1-1)
                self.dp[row1-1][col1-1] = topleft
            else:
                topleft = self.dp[row1-1][col1-1]
        else:
            topleft = 0
        
        if row1 > 0 and col2 >= 0:
            if self.dp[row1-1][col2] == None:
                top = self.getSum(row1-1, col2)
                self.dp[row1-1][col2] = top
            else:
                top = self.dp[row1-1][col2]
        else:
            top = 0
        
        if col1 > 0 and row2 >= 0:
            if self.dp[row2][col1-1] == None:
                left = self.getSum(row2, col1-1) 
                self.dp[row2][col1-1] = left
            else:
                left = self.dp[row2][col1-1]
        else:
            left = 0    
        
        
        if self.dp[row2][col2] == None:
            bottomright = self.getSum(row2, col2)
            self.dp[row2][col2] = bottomright
        else:
            bottomright = self.dp[row2][col2]
        return bottomright - top - left + topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)