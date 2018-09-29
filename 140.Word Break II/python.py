class Solution(object):
    
    def helper(self, s, wlist):
        if s in self.mem:   return self.mem[s]
        ret = []
        for w in wlist:
            if s == w:  
                ret.append(w)
                continue
            if s[:len(w)] == w:
                right = self.helper(s[len(w):], wlist)
                if len(right):
                    for i in right:
                        ret.append(w + " " +i)
        self.mem[s] = ret
        return ret
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.mem = collections.defaultdict(list)
        return self.helper(s, wordDict)