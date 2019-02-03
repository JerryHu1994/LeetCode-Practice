class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        height, width = len(matrix), len(matrix[0])
        startpos = [(0, i) for i in range(width)] + [(i, width-1) for i in range(1, height)]
        ret = []
        for ind, val in enumerate(startpos):
            currlist = []
            y, x = val
            while 0<=y<height and 0<=x<width:
                currlist.append(matrix[y][x])
                y += 1
                x -= 1
            ret.extend(currlist if ind%2 == 1 else currlist[::-1])
        return ret