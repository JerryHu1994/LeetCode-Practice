class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        len_group = list(set([len(w) for w in words]))
        word_set = set(words)
        pairs = []
        currstart, currend = -1, -1
        for i in range(len(S)):
            for l in len_group:
                if i+l <= len(S) and S[i:i+l] in word_set:
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
            ret += S[pre:p[0]] + "<b>" + S[p[0]:p[1]] + "</b>"
            pre = p[1]
        ret += S[pre:]
        return ret