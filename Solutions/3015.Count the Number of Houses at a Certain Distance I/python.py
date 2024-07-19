class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = [[False]*(n+1) for i in range(n+1)]
        for i in range(1,n):
            graph[i][i+1] = True
        for i in range(2, n+1):
            graph[i][i-1] = True
        graph[x][y] = True
        graph[y][x] = True
        self.res = defaultdict(int)
        for i in range(1, n+1):
            self.bfs(i, n, graph)
        return [self.res[i] for i in range(1, n+1)]

    def bfs(self, ind: int, n: int, graph: List[List[int]]):
        queue, visited = [(ind, 0)], set([ind])
        while len(queue) > 0:
            curr = queue.pop(0)
            self.res[curr[1]] += 1
            if curr[1] == n:
                continue
            for nextnode in range(1,n+1):
                if graph[curr[0]][nextnode] and nextnode not in visited:
                    queue.append((nextnode, curr[1]+1))
                    visited.add(nextnode)