class Solution(object):
    def helper(self, s, t):
        tp = 0
        for sp in range(len(s)):
            if t[tp] == s[sp]:  tp += 1
            if tp == len(t):    return True
        return False
            
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ret = ""
        for i in d:
            if self.helper(s, i):
                ret = i if ret=="" or len(i) > len(ret) or (len(i)==len(ret) and i<ret) else ret
        return ret
        