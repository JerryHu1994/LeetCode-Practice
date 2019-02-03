class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        count = 0
        for c in zip(*picture):
            if c.count('B') != N:   continue
            first_row = picture[c.index('B')]
            if first_row.count('B') != N:   continue
            if picture.count(first_row) != N:   continue
            count += 1
        return count*N