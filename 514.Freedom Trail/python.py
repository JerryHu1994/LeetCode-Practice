class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        rlen, klen = len(ring), len(key)
        dic = collections.defaultdict(list)
        # store mapping for each character on each index
        for i in range(rlen):
            for j in range(rlen):
                currdis = min(abs(j-i), rlen-abs(j-i))
                dic[(i, ring[j])].append((j, currdis))
        
        dp = [[0]*rlen for i in range(klen+1)]
        for i in range(klen-1, -1, -1):
            for j in range(rlen):
                dp[i][j] = float("inf")
                for pair in dic[(j, key[i])]:
                    # each change is from i+1
                    dp[i][j] = min(dp[i][j], pair[1]+dp[i+1][pair[0]])
        return dp[0][0]+klen