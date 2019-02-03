class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:  return 0
        if K%2:
            prev = self.kthGrammar(N-1, K//2+1)
            return 0 if prev == 0 else 1
        else:
            prev = self.kthGrammar(N-1, K/2)
            return 1 if prev == 0 else 0
        