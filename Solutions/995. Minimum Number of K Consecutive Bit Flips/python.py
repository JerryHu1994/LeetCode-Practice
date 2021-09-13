class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # curr is number of flips
        n, curr, res = len(A), 0, 0
        for i in range(n):
            if i >= K:
                curr -= A[i-K]/2
            if (curr&1) ^ A[i] == 0:
                if i+K > n: return -1
                A[i] += 2
                curr += 1
                res += 1
        return res