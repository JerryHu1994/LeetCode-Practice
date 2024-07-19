class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def canGoRight(x:int, y:int, visited:set, grid:List[List[int]], q:List[int]):
            if currx+1 < width and (curry, currx+1) not in visited and grid[curry][currx+1] in set([1,3,5]):
                visited.add((curry, currx+1))
                q.append((curry, currx+1))
        def canGoLeft(x:int, y:int, visited:set, grid:List[List[int]], q:List[int]):
            if currx-1 >= 0 and (curry, currx-1) not in visited and grid[curry][currx-1] in set([1, 4, 6]):
                visited.add((curry, currx-1))
                q.append((curry, currx-1))
        def canGoUp(x:int, y:int, visited:set, grid:List[List[int]], q:List[int]):
            if curry-1>=0 and (curry-1, currx) not in visited and grid[curry-1][currx] in set([2, 3, 4]):
                visited.add((curry-1, currx))
                q.append((curry-1, currx))
        def canGoDown(x:int, y:int, visited:set, grid:List[List[int]], q:List[int]):
            if curry+1<height and (curry+1, currx) not in visited and grid[curry+1][currx] in set([2, 5, 6]):
                visited.add((curry+1, currx))
                q.append((curry+1, currx))
        path_dic = defaultdict(list)
        height, width = len(grid), len(grid[0])
        queue = [(0, 0)]
        visited = set([(0, 0)])
        while len(queue):
            curry, currx = queue.pop(0)
            if curry == height-1 and currx == width-1:
                return True
            if grid[curry][currx] == 1:
                canGoRight(currx, curry, visited, grid, queue)
                canGoLeft(currx, curry, visited, grid, queue)
            elif grid[curry][currx] == 2:
                canGoUp(currx, curry, visited, grid, queue)
                canGoDown(currx, curry, visited, grid, queue)
            elif grid[curry][currx] == 3:
                canGoLeft(currx, curry, visited, grid, queue)
                canGoDown(currx, curry, visited, grid, queue)
            elif grid[curry][currx] == 4:
                canGoRight(currx, curry, visited, grid, queue)
                canGoDown(currx, curry, visited, grid, queue)
            elif grid[curry][currx] == 5:
                canGoUp(currx, curry, visited, grid, queue)
                canGoLeft(currx, curry, visited, grid, queue)
            elif grid[curry][currx] == 6:
                canGoUp(currx, curry, visited, grid, queue)
                canGoRight(currx, curry, visited, grid, queue)
        return False

