class Solution(object):
    def helper(self, maze, start, di, visited, queue):
        curr = [start[0], start[1]]
        while 0 <= curr[0]+di[0] < len(maze) and 0 <= curr[1]+di[1] < len(maze[0]) and maze[curr[0]+di[0]][curr[1]+di[1]] != 1:
            curr[0] += di[0]
            curr[1] += di[1]
        if tuple(curr) not in visited:
            queue.append(tuple(curr))
            visited.add(tuple(curr))
    
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = set()
        height, width = len(maze), len(maze[0])
        queue = [(start[0], start[1])]
        visited.add((start[0], start[1]))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue):
            curr = queue.pop(0)
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            for d in dirs:
                self.helper(maze, curr, d, visited, queue)
        return False