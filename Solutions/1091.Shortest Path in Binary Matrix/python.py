class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = [(0,0,1)]
        n = len(grid)
        visited = set()
        visited.add((0,0))
        if grid[0][0] == 1: return -1 
        while len(queue):
            curry, currx, level = queue.pop(0)
            if curry == n-1 and currx == n-1:
                return level
            if curry > 0 and grid[curry-1][currx] == 0 and (curry-1, currx) not in visited:
                queue.append((curry-1, currx, level+1))
                visited.add((curry-1, currx))
            if currx > 0 and grid[curry][currx-1] == 0 and (curry, currx-1) not in visited:
                queue.append((curry, currx-1, level+1))
                visited.add((curry, currx-1))
            if curry < n-1 and grid[curry+1][currx] == 0 and (curry+1, currx) not in visited:
                queue.append((curry+1, currx, level+1))
                visited.add((curry+1, currx))
            if currx < n-1 and grid[curry][currx+1] == 0 and (curry, currx+1) not in visited:
                queue.append((curry, currx+1, level+1))
                visited.add((curry, currx+1))
            if currx > 0 and curry > 0 and grid[curry-1][currx-1] == 0 and (curry-1, currx-1) not in visited:
                queue.append((curry-1, currx-1, level+1))
                visited.add((curry-1, currx-1))
            if currx > 0 and curry < n-1 and grid[curry+1][currx-1] == 0 and (curry+1, currx-1) not in visited:
                queue.append((curry+1, currx-1, level+1))
                visited.add((curry+1, currx-1))
            if curry > 0 and currx < n-1 and grid[curry-1][currx+1] == 0 and (curry-1, currx+1) not in visited:
                queue.append((curry-1, currx+1, level+1))
                visited.add((curry-1, currx+1))
            if curry < n-1 and currx < n-1 and grid[curry+1][currx+1] == 0 and (curry+1, currx+1) not in visited:
                queue.append((curry+1, currx+1, level+1))
                visited.add((curry+1, currx+1))
        return -1