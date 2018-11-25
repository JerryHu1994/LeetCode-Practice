class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue, visited = [(start[0], start[1])], set([(start[0], start[1])])
        height, width = len(maze), len(maze[0])
        def helper(start, di):
            y, x = start
            diy, dix = di
            while 0 <= y+diy < height and 0 <= x+dix < width and maze[y+diy][x+dix] == 0:
                y, x = y + diy, x + dix
            return None if (y,x) == start or (y,x) in visited else (y, x)
        while len(queue):
            y, x = queue.pop()
            if [y, x] == destination:   return True
            nexts = [helper((y, x), [0, -1]), helper((y, x), [-1, 0]), helper((y, x), [0, 1]), helper((y, x), [1, 0])]
            for n in nexts:
                if n != None:
                    queue.append((n[0], n[1]))
                    visited.add((n[0], n[1]))
        return False