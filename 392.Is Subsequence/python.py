class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        currs = 0
        if len(s) == 0: return True
        for ind, val in enumerate(t):
            if val == s[currs]:
                currs+=1
            if currs == len(s):   return True
        return False