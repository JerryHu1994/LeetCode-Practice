class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        ret = [[0]*n for i in range(m)]
        #row
        for i in range(m):
            #col
            for j in range(n):
                #subrow
                count, tempsum = 0, 0
                for a in range(-1, 2):
                    #subcol
                    for b in range(-1, 2):
                        if a + i < 0 or a + i >= m: continue
                        if b + j < 0 or b + j >= n: continue
                        tempsum += M[a + i][b + j]
                        count += 1
                ret[i][j] = int(math.floor(tempsum/count))
        return ret