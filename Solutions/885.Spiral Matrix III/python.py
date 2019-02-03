class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        currlen = 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_idx = 0
        ret = [[r0, c0]]
        curry, currx = r0, c0
        cnt = 0
        while len(ret) < R*C:
            for i in range(currlen):
                curry, currx = curry + dirs[dir_idx][0], currx + dirs[dir_idx][1]
                if 0 <= curry < R and 0 <= currx < C:
                    ret.append([curry, currx])
            cnt += 1
            dir_idx = (dir_idx+1)%len(dirs)
            if cnt == 2:    
                currlen += 1
                cnt = 0
        return ret