class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue = [(i, j)]
                    visited.add((i,j))
                    canWalk = False
                    cnt = 0
                    while len(queue):
                        curri, currj = queue.pop(0)
                        cnt += 1
                        if curri == 0 or curri ==m-1 or currj==0 or currj==n-1:
                            canWalk = True
                        if curri-1>=0 and (curri-1,currj) not in visited and grid[curri-1][currj] == 1:
                            queue.append((curri-1, currj))
                            visited.add((curri-1, currj))
                        if currj-1>=0 and (curri,currj-1) not in visited and grid[curri][currj-1] == 1:
                            queue.append((curri, currj-1))
                            visited.add((curri, currj-1))
                        if curri+1<m and (curri+1,currj) not in visited and grid[curri+1][currj] == 1:
                            queue.append((curri+1, currj))
                            visited.add((curri+1, currj))
                        if currj+1<n and (curri,currj+1) not in visited and grid[curri][currj+1] == 1:
                            queue.append((curri, currj+1))
                            visited.add((curri, currj+1))
                    if not canWalk:
                        ans += cnt
                else:
                    visited.add((i,j))
        return ans