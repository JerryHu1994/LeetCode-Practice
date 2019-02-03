class Solution(object):
    
    def helper(self, triangle, row, col):
        if row == len(triangle)-1:
            return triangle[row][col]
        if (row,col) in self.map:
            return self.map[(row, col)]
        pathSum = triangle[row][col] + min(self.helper(triangle, row+1, col), self.helper(triangle, row+1, col+1))
        self.map[(row, col)] = pathSum
        return pathSum
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.map = {}
        if len(triangle)==0:
            return 0
        return self.helper(triangle, 0, 0)