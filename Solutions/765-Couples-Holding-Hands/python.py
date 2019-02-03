class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)//2
        dsu = DSU(N)
        for i in range(0, len(row), 2):
            first, second = row[i]//2, row[i+1]//2
            dsu.union(first, second)
        return N - sum([i == dsu.find(i)  for i in range(N)])