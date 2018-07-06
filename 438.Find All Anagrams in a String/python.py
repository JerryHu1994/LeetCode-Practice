class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l_s, l_p = len(s), len(p)
        s_count, p_count = collections.Counter(s[0:l_p]), collections.Counter(p)
        ret = []
        for i in range(l_p, l_s):
            if s_count == p_count:
                ret.append(i-l_p)
            if s[i] in s_count:
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1
            s_count[s[i-l_p]] -= 1
            if s_count[s[i-l_p]] == 0:  del s_count[s[i-l_p]]
        if s_count == p_count:  ret.append(l_s-l_p)
        return ret