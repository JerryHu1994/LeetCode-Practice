class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        ret = [1]
        while len(ret) < N:
            # odd + even
            ret = [i*2-1 for i in ret] + [i*2 for i in ret]
        return [i for i in ret if i <= N]