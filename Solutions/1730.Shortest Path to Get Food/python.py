class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def validate(curry, currx):
            if curry < 0 or curry >= height or currx < 0 or currx >= width:
                return False
            if (curry, currx) in visited:
                return False
            if grid[curry][currx] == 'X':
                return False
            return True
        starty, startx = None, None
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "*":
                    starty, startx = y, x
        queue = [(starty, startx, 0)]
        height, width = len(grid), len(grid[0])
        ans = 0
        visited = set()
        visited.add((starty, startx))
        while len(queue) != 0:
            curry, currx, currdis = queue.pop(0)
            if grid[curry][currx] == '#':   return currdis
            neighbors = [(curry-1, currx, currdis+1), (curry+1, currx, currdis+1), (curry, currx-1, currdis+1), (curry, currx+1, currdis+1)]
            for pair in neighbors:
                coord = (pair[0], pair[1])
                if validate(coord[0], coord[1]):
                    queue.append(pair)
                    visited.add(coord)
        return -1
                