class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = int(math.ceil((-1+math.sqrt(1+8*target))/2))
        s = (1+n)*n/2
        if (s-target)%2 == 0:   return n
        # diff is odd
        return n+1  if (n+1)%2 == 1 else n+2