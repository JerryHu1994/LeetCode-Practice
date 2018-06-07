class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #set two flags for first row and first column
        first_row, first_col = False, False
        w,h = len(matrix[0]), len(matrix)
        for i in range(0,w):
            if matrix[0][i] == 0:
                first_row = True
                break
        for i in range(0, h):
            if matrix[i][0] == 0:
                first_col = True
                break
        # set zero flags
        for i in range(1,h):
            for j in range(1,w):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, w):
            if matrix[0][i] == 0:
                # set col i to zero
                for j in range(0,h):
                    matrix[j][i] = 0
        for i in range(1,h):
            if matrix[i][0] == 0:
                # set row i to zero
                for j in range(0,w):
                    matrix[i][j] = 0
        # set first row to zero if necessary
        if first_row:
            for i in range(0, w):
                matrix[0][i] = 0
        if first_col:
            for i in range(0,h):
                matrix[i][0] = 0