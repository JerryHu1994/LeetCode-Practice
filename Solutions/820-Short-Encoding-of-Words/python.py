class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        reverse = []
        for w in words: reverse.append(w[::-1])
        sort = sorted(reverse)
        ret = 0
        ind = 0
        while ind < len(sort):
            if ind < len(sort)-1:
                if len(sort[ind]) <= len(sort[ind+1]) and sort[ind] == sort[ind+1][:len(sort[ind])]:
                    ind += 1
                    continue
            ret += len(sort[ind])+1
            ind += 1
        return ret