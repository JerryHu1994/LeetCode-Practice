class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        ans = 0
        height, width = len(isWater), len(isWater[0])
        visited = [[0]*width for i in range(height)]
        ans = [[0]*width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = 1
        
        while len(queue) > 0:
            (curry, currx) = queue.pop(0)
            if curry > 0 and visited[curry-1][currx] == 0:
                queue.append((curry-1, currx))
                visited[curry-1][currx] = 1
                ans[curry-1][currx] = ans[curry][currx] + 1
            if curry<height-1 and visited[curry+1][currx] == 0:
                queue.append((curry+1, currx))
                visited[curry+1][currx] = 1
                ans[curry+1][currx] = ans[curry][currx] + 1
            if currx > 0 and visited[curry][currx-1] == 0:
                queue.append((curry, currx-1))
                visited[curry][currx-1] = 1
                ans[curry][currx-1] = ans[curry][currx] + 1
            if currx < width-1 and visited[curry][currx+1] == 0:
                queue.append((curry, currx+1))
                visited[curry][currx+1] = 1
                ans[curry][currx+1] = ans[curry][currx] + 1
        return ans