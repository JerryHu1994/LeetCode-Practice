class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        len_group = list(set([len(w) for w in dict]))
        word_set = set(dict)
        pairs = []
        currstart, currend = -1, -1
        for i in range(len(s)):
            for l in len_group:
                if i+l <= len(s) and s[i:i+l] in word_set:
                    if currstart == -1:  currstart = i
                    currend = max(currend, i+l)
            if i >= currend and currstart != -1:
                # stop and save the pair
                pairs.append((currstart, currend))
                currstart, currend = -1, -1
        if currstart != -1: pairs.append((currstart, currend))
        ret = ""
        pre = 0
        for p in pairs:
            ret += s[pre:p[0]] + "<b>" + s[p[0]:p[1]] + "</b>"
            pre = p[1]
        ret += s[pre:]
        return ret