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
            chars = [c.upper()  for c in w]
            set_ind = None
            for i in range(3):
                if chars[0] in sets[i]:
                    set_ind = i
                    break
            for c in chars:
                if c not in sets[set_ind]:
                    break
            else:
                ret.append(w)
        return ret