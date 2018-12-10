class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        unitlen = numRows + numRows - 2
        strlist = []
        while len(s):
            strlist.append([i for i in s[:unitlen]])
            s = s[unitlen:]
        ret = ""
        # get top row off
        l = len(strlist)
        for i in range(l):
            ret += strlist[i].pop(0)
        unitlen -= 1
        while unitlen > 1:
            for i in range(l):
                if len(strlist[i]) == unitlen:
                    ret += strlist[i].pop(0)
                    ret += strlist[i].pop()
                else:
                    if len(strlist[i]) > 0:
                        ret += strlist[i].pop(0)
            unitlen -= 2
        # get last row off
        for i in range(l):
            if len(strlist[i]):
                ret += strlist[i].pop(0)
        return ret