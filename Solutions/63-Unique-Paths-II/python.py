class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0] == 1:  return 0
        pathmap = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: 
                    pathmap[i][j] = 0
                else:
                    if i==0 and j ==0: 
                        pathmap[i][j] = 1
                        continue
                    if i==0:
                        pathmap[i][j] += pathmap[i][j-1]
                        continue
                    if j==0:
                        pathmap[i][j] += pathmap[i-1][j]
                        continue
                    pathmap[i][j] += pathmap[i-1][j] + pathmap[i][j-1]
        return pathmap[m-1][n-1]
                