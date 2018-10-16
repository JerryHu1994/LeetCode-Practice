class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        culsum, curr = [], 0
        for i in A:
            curr += i
            culsum.append(curr)
        # pre[i] means largest presum from 0 to somewhere before or include i
        premax, curr = [], float("-inf")
        for i in culsum:
            curr = max(curr, i)
            premax.append(curr)
        # postmax means largest presum from i to somewhere before or include end
        postmax = []
        curr = float("-inf")
        for i in range(len(A)-1, -1, -1):
            curr = max(culsum[i], curr)
            postmax.append(curr-culsum[i-1] if i > 0 else curr)
        postmax = postmax[::-1]
        ret = float("-inf")
        for i in range(len(A)):
            pmax = postmax[i]
            circularmax = culsum[-1] - (culsum[i-1] if i != 0 else 0) + (0 if i==0 else premax[i-1])
            ret = max([pmax, circularmax, ret])
        return ret
        