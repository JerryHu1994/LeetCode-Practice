class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0: return len(s) == 0
        firstmatch = len(s)!=0 and (s[0] == p[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (firstmatch and self.isMatch(s[1:], p))
        else:
            return firstmatch and self.isMatch(s[1:], p[1:])