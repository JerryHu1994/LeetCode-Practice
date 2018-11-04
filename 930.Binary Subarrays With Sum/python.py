class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        ret, n = 0, len(A)
        if sum(A) == 0:
            return 0 if S != 0 else n*(n+1)/2
        ones = [ind for ind, val in enumerate(A) if val == 1]
        if len(ones) < S:   return 0
        left_zeros, right_zeros = [], []
        for i in range(len(ones)):
            left_zeros.append(ones[i] if i == 0 else ones[i]-ones[i-1]-1)
        right_zeros = left_zeros[1:] + [n-1-ones[-1]]
        # if S == 0, special case
        if S == 0:
            all_zeros = left_zeros + [n-1-ones[-1]]
            return sum([i*(i+1)/2 for i in all_zeros])
        for i in range(len(ones)-S+1):
            ret += (left_zeros[i]+1) * (right_zeros[i+S-1]+1)
        return ret