class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows == 0:    return ret
        ret.append([1])
        if numRows == 1:    return ret
        for i in range(numRows-1):
            curr = 0
            lastrow = ret[-1]
            nextrow = []
            for i in range(0, len(lastrow)-1):
                nextrow.append(lastrow[i] + lastrow[i+1])
            ret.append([1] + nextrow + [1])
        return ret