class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:  return -1
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        connected_componentcount = 0
        visited = set()
        def bfs(index):
            queue = [index]
            visited.add(index)
            while len(queue):
                curridx = queue.pop(0)
                for nextindex in graph[curridx]:
                    if nextindex not in visited:
                        queue.append(nextindex)
                        visited.add(nextindex)
        for i in range(n):
            if i not in visited:
                bfs(i)
                connected_componentcount += 1
        return  connected_componentcount - 1