class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        ydic = defaultdict(int)
        xdic = defaultdict(int)
        serverlist = []
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    ydic[y] += 1
                    xdic[x] += 1
                    serverlist.append((y,x))
        ans = 0
        for y, x in serverlist:
            if ydic[y] == 1 and xdic[x] == 1:
                ans += 1
        return len(serverlist) - ans