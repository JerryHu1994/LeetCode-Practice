class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if len(strs)==0:    return ret
        for i in range(len(strs[0])):
            currc = strs[0][i]
            for s in strs[1:]:
                if len(s) < i+1:
                    return ret
                else:
                    if s[i] != currc:
                        return ret
            ret += currc
        return ret