class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ''
        while len(s) > 0:
            rev = s[0:2*k]
            s = s[2*k:]
            if rev < k:
                ret += rev[::-1]
            else:
                ret += rev[0:k][::-1] + rev[k:]
        return ret
                