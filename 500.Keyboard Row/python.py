class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"}
        set2 = {"A", "S", "D", "F", "G", "H", "J", "K", "L"}
        set3 = {"Z", "X", "C", "V", "B", "N", "M"}
        ret = []
        sets = [set1, set2, set3]
        for w in words:
            found = False
            for s in sets:
                for ind, c in enumerate(w):
                    if c.upper() not in s:
                        break
                    if ind == len(w)-1:
                        found = True
                        ret.append(w)
                if found:   break
        return ret
            
                    
                    