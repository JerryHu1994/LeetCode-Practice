class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        # create value to idx mapping
        dic = {val:ind for ind, val in enumerate(A)}
        dp = [[2]*l for i in range(l)]
        for k in range(l):
            for j in range(k):
                i = dic.get(A[k] - A[j], None)
                if i != None and i < j:
                    #dp relation: only when A[i] + A[j] == A[k], we have a valid connection
                    dp[k][j] = max(dp[k][j], dp[j][i]+1)
        ret = max([max(i) for i in dp])
        return 0 if ret == 2 else ret
        