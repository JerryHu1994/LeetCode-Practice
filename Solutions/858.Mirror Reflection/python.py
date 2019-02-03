from fractions import gcd
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        g = gcd(p, q)
        pp, qq = (p/g)%2, (q/g)%2
        if pp and qq:
            return 1
        elif pp:
            return 0
        else:
            return 2