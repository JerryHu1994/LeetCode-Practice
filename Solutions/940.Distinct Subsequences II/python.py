class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]
        dic = {}
        for ind, c in enumerate(S):
            currcnt = dp[-1]*2
            if c in dic:
                dp.append(currcnt - dp[dic[c]])
            else:
                dp.append(currcnt)
            dic[c] = ind
        return (dp[-1]-1)%(10**9+7)