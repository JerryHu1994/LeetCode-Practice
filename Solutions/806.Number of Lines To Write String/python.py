class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        currwidth, currcount = 0, 0
        linecount = 0
        for i in range(len(S)):
            curridx = ord(S[i]) - ord('a')
            # check if overflows
            if currwidth + widths[curridx] > 100:
                linecount += 1
                currwidth = widths[curridx]
                currcount = 1
            else:
                currwidth += widths[curridx]
                currcount += 1
        ret = []
        if currcount != 0:
            ret.append(linecount+1)
        ret.append(currwidth)
        return ret
            