class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                ma, mi = "", ""
                if len(s) >= len(t):
                    ma,mi = s,t
                else:
                    ma,mi = t,s
                # insert
                if mi[0:i]+ma[i]+mi[i:] == ma:
                    return True
                # delete
                if ma[0:i]+ma[i+1:] == mi:
                    return True
                # replace
                if mi[0:i]+ma[i]+mi[i+1:] == ma:
                    return True
                return False
        return abs(len(s) - len(t)) == 1