class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 10**9+7
        dic = {1: [6, 8], 2:[7, 9], 3: [4, 8], 4:[3, 9, 0], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2, 4], 0:[4, 6]}
        currcnt = [1]*10
        for i in range(N-1):
            nextcnt = [0]*10
            for j in range(10):
                if j not in dic:    continue
                for k in dic[j]:
                    nextcnt[k] += currcnt[j]
            currcnt = nextcnt
        return sum(currcnt)%mod