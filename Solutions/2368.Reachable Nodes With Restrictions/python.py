class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restrictset = set(restricted)
        edgemap = defaultdict(list)
        for pointa, pointb in edges:
            edgemap[pointa].append(pointb)
            edgemap[pointb].append(pointa)
        visited = set()
        visited.add(0)
        queue = [0]
        while len(queue):
            curr = queue.pop(0)
            for nextpoint in edgemap[curr]:
                if nextpoint not in visited and nextpoint not in restrictset:
                    queue.append(nextpoint)
                    visited.add(nextpoint)
        return len(visited)