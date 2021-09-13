class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def helper(cnt):
            count = collections.Counter()
            res = l = 0
            for r in range(len(A)):
                if count[A[r]] == 0:    cnt -= 1
                # each time increment right
                count[A[r]] += 1
                # each time when more than cnt char is observed, keep move left until cnt is non-neg
                while cnt < 0:
                    count[A[l]] -= 1
                    if count[A[l]] == 0:    cnt += 1
                    l += 1
                res += r - l + 1
            return res
        return helper(K) - helper(K-1)
        