class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for i in range(1, N+1):
            s = set([int(j) for j in str(i)])
            if 3 in s or 4 in s or 7 in s:  continue
            if (2 not in s) and (5 not in s) and (6 not in s) and (9 not in s): continue
            ret += 1
        return ret