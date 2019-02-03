class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:  return [i for i in range(10)]
        if K == 0:  return [int(str(i)*N) for i in range(1, 10)]
        self.ans = []
        def helper(prenum):
            if len(prenum) == N:
                self.ans.append(int(prenum))
                return
            last_digit = int(prenum[-1])
            if last_digit+K < 10:
                helper(prenum+str(last_digit+K))
            if last_digit-K >= 0:
                helper(prenum+str(last_digit-K))
        for i in range(1, 10):
            helper(str(i))
        return self.ans