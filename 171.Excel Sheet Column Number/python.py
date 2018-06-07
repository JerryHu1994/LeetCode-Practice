class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,ret = len(s),0
        for idx,val in enumerate(s):
            ret += (ord(val) - ord('A') + 1) * (26**(l-1-idx))
        return ret