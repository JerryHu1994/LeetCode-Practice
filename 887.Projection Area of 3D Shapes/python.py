class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        top = 0
        for l in grid:
            for i in l:
                if i != 0:
                    top += 1
        front = sum([max(i) for i in grid])
        left = 0
        for i in zip(*grid):
            left += max(i)
        print top, front, left
        return top+front+left
        