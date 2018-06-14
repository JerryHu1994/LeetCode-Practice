class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:  return True
        m = int(math.ceil(math.sqrt(c)))
        for i in range(0,m):
            rest = c - i**2
            sx = math.sqrt(rest)
            if round(sx) == sx:
                return True
        return False