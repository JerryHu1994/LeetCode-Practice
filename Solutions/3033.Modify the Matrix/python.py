class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for col in range(n):
            max_ele = max([matrix[row][col] for row in range(m) if matrix[row][col] != -1])
            for row in range(m):
                if matrix[row][col] == -1:
                    matrix[row][col] = max_ele
        return matrix