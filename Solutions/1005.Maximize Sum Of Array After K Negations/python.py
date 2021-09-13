class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        abs_arr = [abs(i) for i in A]
        min_val = min(abs_arr)
        A = sorted(A)
        neg_cnt = len([i for i in A if i < 0])
        if K <= neg_cnt:
            return -sum(A[:K]) + sum(A[K:])
        else:
            return sum(abs_arr) - min_val + (-min_val if (K-neg_cnt) % 2 == 1 else min_val)