class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def getParent(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        px, py = self.getParent(x), self.getParent(y)
        self.parents[px] = py

class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        totalsize = N*N*4
        dsu = DSU(totalsize)
        getid = lambda x,y,z : y*N*4+x*4+z
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                # 0-left, 1-top, 2-right, 3-bottom
                if x > 0:   dsu.union(getid(y, x, 0), getid(y, x-1, 2))
                if y > 0:   dsu.union(getid(y, x, 1), getid(y-1, x, 3))
                if x < N-1: dsu.union(getid(y, x, 2), getid(y, x+1, 0))
                if y < N-1: dsu.union(getid(y, x, 3), getid(y+1, x, 1))
                if val in '/ ':
                    dsu.union(getid(y,x,0), getid(y,x,1))
                    dsu.union(getid(y,x,2), getid(y,x,3))
                if val in '\ ':
                    dsu.union(getid(y,x,1), getid(y,x,2))
                    dsu.union(getid(y,x,0), getid(y,x,3))
        return sum([dsu.getParent(x) == x for x in range(totalsize)])