class Solution(object):
    def helper(self, maze, start, di, diname, history, queue, destination):
        curr = [start[0], start[1]]
        currdis, currpath = start[2], start[3]
        move = False
        while 0 <= curr[0]+di[0] < len(maze) and 0 <= curr[1]+di[1] < len(maze[0]) and maze[curr[0]+di[0]][curr[1]+di[1]] != 1:
            curr[0] += di[0]
            curr[1] += di[1]
            currdis += 1
            move = True
            # check if hit the hole
            if curr[0] == destination[0] and curr[1] == destination[1]:
                if currdis < self.beststeps or (currdis == self.beststeps and currpath+diname < self.bestpath):
                    self.beststeps = currdis
                    self.bestpath = currpath+diname
                    return
        currpath = currpath + diname if move else currpath
        his = history[curr[0]][curr[1]]
        if not move:    return
        if his == None or his[0] > currdis or (his[0] == currdis and currpath < his[1]):
            queue.append(tuple(curr+[currdis, currpath]))
            history[curr[0]][curr[1]] = (currdis, currpath)

    def findShortestWay(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        height, width = len(maze), len(maze[0])
        queue = [(start[0], start[1], 0, "")]
        history = [[None]*width for i in range(height)]
        history[start[0]][start[1]] = (0, "")
        self.bestpath, self.beststeps = None, float("inf")
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dirname = ['u', 'd', 'l', 'r']
        while len(queue):
            curr = queue.pop(0)
            for ind in range(4):
                self.helper(maze, curr, dirs[ind], dirname[ind], history, queue, destination)
        return "impossible" if self.bestpath == None else self.bestpath