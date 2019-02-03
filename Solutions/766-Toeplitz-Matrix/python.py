class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        height, width = len(matrix), len(matrix[0])
        start = [[0, i] for i in range(width)] + [[i, 0] for i in range(1, height)]
        for p in start:
            ele, curr = matrix[p[0]][p[1]], p
            while True:
                if matrix[curr[0]][curr[1]] != ele:
                    return False
                curr[0] += 1
                curr[1] += 1
                if curr[0] >= height or curr[1] >= width:
                    break
        return True
                