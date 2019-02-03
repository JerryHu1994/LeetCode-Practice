class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.dic = {}
        self.valset = set()
        def helper(pa, s):
            if len(pa) == 0 and len(s) == 0:    return True
            if len(pa) == 0 or len(s) == 0: return False
            if pa[0] in self.dic:
                l = len(self.dic[pa[0]])
                if self.dic[pa[0]] != s[0:l]:
                    return False
                else:
                    return helper(pa[1:], s[l:])
            # first char never seen before
            for i in range(1, len(s)+1):
                if s[:i] in self.valset:    continue
                self.dic[pa[0]] = s[:i]
                self.valset.add(s[:i])
                ret = helper(pa[1:], s[i:])
                if ret:
                    return ret
                else:
                    del self.dic[pa[0]]
                    self.valset.remove(s[:i])
            return False
        return helper(pattern, str)
        