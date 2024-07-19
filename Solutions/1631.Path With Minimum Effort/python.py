class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, height = len(heights[0]), len(heights)
        dist = [[float("inf")]*row for h in range(height)]
        dist[0][0] = 0
        h = []
        heappush(h, (0, 0, 0))
        while len(h):
            curr_effort, y, x = heappop(h)
            if y > 0 and max(curr_effort, abs(heights[y-1][x]-heights[y][x])) < dist[y-1][x]:
                dist[y-1][x] = max(curr_effort, abs(heights[y-1][x]-heights[y][x]))
                heappush(h, (dist[y-1][x], y-1, x))
            if y < height-1 and max(curr_effort, abs(heights[y+1][x]-heights[y][x])) < dist[y+1][x]:
                dist[y+1][x] = max(curr_effort, abs(heights[y+1][x]-heights[y][x]))
                heappush(h, (dist[y+1][x], y+1, x))
            if x > 0 and max(curr_effort, abs(heights[y][x-1]-heights[y][x])) < dist[y][x-1]:
                dist[y][x-1] = max(curr_effort, abs(heights[y][x-1]-heights[y][x]))
                heappush(h, (dist[y][x-1], y, x-1))
            if x < row-1 and max(curr_effort, abs(heights[y][x+1]-heights[y][x])) < dist[y][x+1]:
                dist[y][x+1] = max(curr_effort, abs(heights[y][x+1]-heights[y][x]))
                heappush(h, (dist[y][x+1], y, x+1))
        return dist[-1][-1]