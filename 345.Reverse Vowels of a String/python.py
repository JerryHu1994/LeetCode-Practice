class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:   return s
        ret = [i for i in s]
        se = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        l, r = 0, len(s)-1
        while l < r:
            while l<len(s) and s[l] not in se:    l+=1
            while r>0 and s[r] not in se:    r-=1
            if l<r:
                ret[l], ret[r] = ret[r], ret[l]
            l+=1
            r-=1
        return "".join(ret)