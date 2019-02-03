class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for ind, val in enumerate(order):
            dic[val] = ind
        def compare(w1, w2):
            p = 0
            while p < len(w1) and p < len(w2) and w1[p] == w2[p]:
                p += 1
            if p < len(w1) and p < len(w2):
                return dic[w1[p]] < dic[w2[p]]
            else:
                return len(w1) <= len(w2)
            
        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True