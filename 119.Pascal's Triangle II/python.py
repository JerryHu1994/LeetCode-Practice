class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:   return [1]
        curr = [1,1]
        if rowIndex == 1:   return curr
        for i in range(1, rowIndex):
            n = []
            for i in range(len(curr)-1):
                n.append(curr[i]+curr[i+1])
            curr = [1] + n + [1]
        return curr