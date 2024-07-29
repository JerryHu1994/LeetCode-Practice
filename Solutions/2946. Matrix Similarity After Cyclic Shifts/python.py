class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        remain = k % n
        for ind, row in enumerate(mat):
            if ind % 2 == 0:
                newrow = row[remain:] + row[:remain]
            else:
                newrow = row[-remain:] + row[:-remain]
            for i in range(n):
                if newrow[i] != row[i]: return False
        return True