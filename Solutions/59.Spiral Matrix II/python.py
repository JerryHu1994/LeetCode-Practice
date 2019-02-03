class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ret = [[0]*n for i in range(n)]
        visited = [[False]*n for i in range(n)]
        i, dir_idx, currx, curry = 1, 0, -1, 0
        while i < n**2+1:
            ydir, xdir = dirs[dir_idx]
            
            if currx + xdir < 0 or currx + xdir >= n or curry + ydir < 0 or curry + ydir >= n or visited[curry + ydir][currx + xdir]:
                # change direction
                dir_idx = (dir_idx + 1) % len(dirs)
                continue
            currx, curry = currx + xdir, curry + ydir
            ret[curry][currx] = i
            visited[curry][currx] = True
            i += 1
        return ret