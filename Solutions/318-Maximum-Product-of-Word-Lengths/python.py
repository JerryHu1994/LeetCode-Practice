class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask = [0]*len(words)
        for i in range(len(words)):
            for j in words[i]:
                mask[i] |= 1<<(ord(j) - ord("a"))
        ret = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if mask[i] & mask[j] == 0 and len(words[i])*len(words[j]) > ret:
                    ret = len(words[i])*len(words[j])
        return ret