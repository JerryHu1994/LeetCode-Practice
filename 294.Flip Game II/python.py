class Solution(object):
    def helper(self, s):
        if s in self.dic:
            return self.dic[s]
        for ind, val in enumerate(s):
            if ind == len(s)-1: continue
            if val=="+" and s[ind+1]=="+":
                if not self.helper(s[0:ind] + "--" + s[ind+2:]):
                    self.dic[s] = True
                    return True
        self.dic[s] = False
        return False
    
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.dic = {}
        return self.helper(s)
        
        