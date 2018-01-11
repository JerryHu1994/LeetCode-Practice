class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pathmap = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):  pathmap[i][0] = 1
        for j in range(n):  pathmap[0][j] = 1
        for i in range(1,m,1):
            for j in range(1,n,1):
                pathmap[i][j] = pathmap[i-1][j] + pathmap[i][j-1]
        return pathmap[m-1][n-1]