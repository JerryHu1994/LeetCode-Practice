class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:    return False
        height, width = len(matrix), len(matrix[0])
        currx, curry = width-1, 0
        while True:
            if curry >= height or currx < 0:
                break
            if matrix[curry][currx] == target:
                return True
            elif matrix[curry][currx] < target:
                curry += 1
            else:
                currx -= 1
        return False