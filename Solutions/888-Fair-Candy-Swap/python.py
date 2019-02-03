class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a, sum_b = sum(A), sum(B)
        diff = sum_a - sum_b
        set_a, set_b = set(A), set(B)
        for a in set_a:
            if a-diff/2 in set_b:
                return [a, a-diff/2]