class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ind1, ind2 = float("-inf"), float("-inf")
        ret = float("inf")
        for i,w in enumerate(words):
            if w == word1:
                ind1 = i
                ret = min(ind1-ind2, ret)
            elif w == word2:
                ind2 = i
                ret = min(ind2-ind1, ret)
        return ret
            
            