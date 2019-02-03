class Solution(object):
    def helper(self, maze, start, di, history, queue):
        curr = [start[0], start[1]]
        currdis = start[2]
        while 0 <= curr[0]+di[0] < len(maze) and 0 <= curr[1]+di[1] < len(maze[0]) and maze[curr[0]+di[0]][curr[1]+di[1]] != 1:
            curr[0] += di[0]
            curr[1] += di[1]
            currdis += 1
        if currdis < history[curr[0]][curr[1]]:
            queue.append(tuple(curr+[currdis]))
            history[curr[0]][curr[1]] = currdis

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        height, width = len(maze), len(maze[0])
        queue = [(start[0], start[1], 0)]
        history = [[float("inf")]*width for i in range(height)]
        history[start[0]][start[1]] = 0
        self.ret = float("inf")
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue):
            curr = queue.pop(0)
            if curr[0] == destination[0] and curr[1] == destination[1]:
                self.ret = min(self.ret, curr[2])
                continue
            for d in dirs:
                self.helper(maze, curr, d, history, queue)
        return -1 if self.ret == float("inf") else self.ret