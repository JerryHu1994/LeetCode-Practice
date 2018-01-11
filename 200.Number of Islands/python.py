class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (not len(grid)) or (not len(grid[0])):
            return 0
        rows, cols, ret = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    #do a bfs and mark all 1 as 0
                    queue = [(j,i)]
                    grid[i][j] = 0
                    ret+=1
                    while len(queue):
                        curr = queue.pop(0)
                        currx, curry = curr[0], curr[1]
                        if currx+1 < cols and grid[curry][currx+1]=="1":
                            queue.append((currx+1,curry))
                            grid[curry][currx+1] = 0
                        if curry+1<rows and grid[curry+1][currx]=="1":
                            queue.append((currx,curry+1))
                            grid[curry+1][currx] = 0
                        if curry-1>=0 and grid[curry-1][currx]=="1":
                            queue.append((currx,curry-1))
                            grid[curry-1][currx] = 0
                        if currx-1>=0 and grid[curry][currx-1]=="1":
                            queue.append((currx-1,curry))
                            grid[curry][currx-1] = 0
                        
        return ret
                    