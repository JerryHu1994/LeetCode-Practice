class Solution(object):
    def helper(self, w1, w2):
        if (w1, w2) in self.dic:
            return self.dic[(w1, w2)]
        if len(w1) == 0 and len(w2) == 0:
            return 0
        if len(w1) == 0:
            return len(w2)
        if len(w2) == 0:
            return len(w1)
        ret = 0
        if w1[0] == w2[0]:
            ret = self.helper(w1[1:], w2[1:])
        else:
            dw1 = 1+self.helper(w1[1:], w2)
            dw2 = 1+self.helper(w1, w2[1:])
            ret = min(dw1, dw2)
        self.dic[(w1, w2)] = ret
        return ret
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.dic = {}
        return self.helper(word1, word2)