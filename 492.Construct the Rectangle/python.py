class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #bestdiff = float("inf")
        upper = int(math.floor(math.sqrt(area)))
        for i in range(upper, 0, -1):
            if area%i == 0:
                return [area/i, i]