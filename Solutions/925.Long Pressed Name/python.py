class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        def helper(string):
            if len(string) == 0:    return []
            ret, curr = [], 1
            for ind in range(1, len(string)):
                if string[ind] == string[ind-1]:
                    curr += 1
                else:
                    ret.append((string[ind-1], curr))
                    curr = 1
            ret.append((string[-1], curr))
            return ret
        namestr, typedstr = helper(name), helper(typed)
        if len(namestr) != len(typedstr):   return False
        for i in range(len(namestr)):
            if namestr[i][1] > typedstr[i][1]:  return False
        return True