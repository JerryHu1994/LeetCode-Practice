class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        visited = set()
        height, width = len(grid), len(grid[0])
        queue = []
        finalkeys = 0
        directs = [-1, 0, 1, 0, -1]
        # find the initial position and number of keys
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "@":
                    currstate = (i, j, 0)
                    queue.append(currstate)
                    visited.add(currstate)
                elif 'a' <= grid[i][j] <= 'f':
                    finalkeys |= (1 << (ord(grid[i][j]) - ord('a')))
        step = 0
        while len(queue):
            currlen = len(queue)
            for i in range(currlen):
                curr = queue.pop(0)
                currkey = curr[2]
                # check for final state
                if curr[2] == finalkeys:    return step
                for d in range(4):
                    nextx, nexty, newkey = curr[1]+directs[d], curr[0]+directs[d+1], currkey
                    if nextx < 0 or nextx >= width or nexty < 0 or nexty >= height or grid[nexty][nextx] == "#": continue # out of bound
                    if "A" <= grid[nexty][nextx] <= "F" and not (currkey & (1 << (ord(grid[nexty][nextx])-ord("A")))):    continue # lock without keys, skip
                    if "a" <= grid[nexty][nextx] <= "f":    newkey |= (1 << (ord(grid[nexty][nextx])-ord("a"))) # add a key
                    newstate = (nexty, nextx, newkey)
                    if newstate in visited: continue
                    queue.append(newstate)
                    visited.add(newstate)
            step += 1 
        return -1