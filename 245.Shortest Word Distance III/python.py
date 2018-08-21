class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev, prevword, ret = None, None, float("inf")
        for ind, w in enumerate(words):
            if w == word1:
                if prevword == word2:
                    ret = min(ret, ind - prev)
                prev = ind
                prevword = word1
                    
            elif w == word2:
                if prevword == word1:
                    ret = min(ret, ind - prev)
                prev = ind
                prevword = word2
        return ret