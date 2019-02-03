class Solution(object):
    def helper(self, word1, word2):
        if (word1, word2) in self.dic:
            return self.dic[(word1, word2)]
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1[0] == word2[0]:
            ret = self.helper(word1[1:], word2[1:])
            self.dic[(word1, word2)] = ret
            return ret
        insert = 1 + self.helper(word1, word2[1:])
        delete = 1 + self.helper(word1[1:], word2)
        replace = 1 + self.helper(word1[1:], word2[1:])
        ret = min(insert, delete, replace)
        self.dic[(word1, word2)] = ret
        return ret
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.dic = {}
        return self.helper(word1, word2)