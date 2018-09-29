class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        stack = []
        ret = 0
        for i,val in enumerate(A):
            while len(stack) > 0 and val < stack[-1][0]:    stack.pop()
            if len(stack) == 0:
                s = (i+1)*val
            else:
                s = stack[-1][2] + val*(i-stack[-1][1])
            ret += s
            stack.append((val, i, s))
        return ret % (10**9+7)