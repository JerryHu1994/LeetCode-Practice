class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_split = str.split()
        if len(pattern) != len(str_split):
            return False
        dic = {}
        dup = set()
        for i, v in enumerate(pattern):
            if not v in dic:
                if str_split[i] in dup:
                    return False
                dic[v] = str_split[i]
                dup.add(str_split[i])
            else:
                if dic[v] != str_split[i]:
                    return False
        return True