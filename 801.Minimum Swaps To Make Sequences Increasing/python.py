class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = len(A)
        keep, swap = [float("inf")]*l, [float("inf")]*l # if we keep/swap ith, how many swaps will be
        swap[0] = 1
        keep[0] = 0
        for i in range(1,l):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                keep[i] = min(swap[i-1], keep[i])
                swap[i] = min(swap[i], keep[i-1]+1)
        return min(keep[-1], swap[-1])