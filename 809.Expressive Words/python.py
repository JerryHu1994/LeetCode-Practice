class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def helper(w):
            p = 0
            ret = []
            while p < len(w):
                start = p
                while p+1 < len(w) and w[p] == w[p+1]:
                    p += 1
                ret.append(w[start:p+1])
                p += 1
            return ret
        ptr = 0
        s_segs = helper(S)
        ret = 0
        for word in words:
            word_segs = helper(word)
            if len(s_segs) != len(word_segs):   continue
            for i in range(len(s_segs)):
                if s_segs[i] == word_segs[i] or (len(s_segs[i])>=3 and s_segs[i][0] == word_segs[i][0] and len(word_segs[i]) < len(s_segs[i])):
                    continue
                else:
                    break
            else:
                ret += 1
        return ret