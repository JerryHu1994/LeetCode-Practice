class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = {}
        se = set()
        for ind, val in enumerate(s):
            if val in dic:
                if dic[val] != t[ind]:
                    return False
            else:
                if t[ind] in se:
                    return False
                dic[val] = t[ind]
                se.add(t[ind])
        return True
        
                