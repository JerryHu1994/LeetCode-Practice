class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if len(picture) == 0 or len(picture[0]) == 0:   return 0
        height, width = len(picture), len(picture[0])
        ret = 0
        rowcount, colcount = [0]*height, [0]*width
        for i in range(height):
            for j in range(width):
                if picture[i][j] == "B":
                    rowcount[i] += 1
                    colcount[j] += 1
        for i in range(height):
            for j in range(width):
                if picture[i][j] == "B" and rowcount[i] == 1 and colcount[j] == 1:
                    ret +=1
        return ret