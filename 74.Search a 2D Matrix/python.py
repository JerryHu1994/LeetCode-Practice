class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0: return False
        width, height = len(matrix[0]), len(matrix)
        i, j = width-1, 0
        while True:
            if i<0 or j>=height:    break
            if matrix[j][i] == target:  return True
            if matrix[j][i] < target:
                #move down
                j+=1
            else:
                #move left
                i-=1
        return False
        