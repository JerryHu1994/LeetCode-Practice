class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(set)
        for edge_a, edge_b in edges:
            dic[edge_a].add(edge_b)
            dic[edge_b].add(edge_a)
        queue = [0]
        visited = set()
        furtherest_node = 0
        while len(queue):
            nextq = []
            for currnode in queue:
                visited.add(currnode)
                for nextnode in dic[currnode]:
                    if nextnode not in visited:
                        nextq.append(nextnode)
            furtherest_node = nextq[0] if len(nextq) > 0 else furtherest_node
            queue = nextq
        # bfs from furtherest
        queue = [furtherest_node]
        visited = set()
        level = 0
        while len(queue):
            nextq = []
            for currnode in queue:
                visited.add(currnode)
                for nextnode in dic[currnode]:
                    if nextnode not in visited:
                        nextq.append(nextnode)
            if len(nextq) > 0:  level += 1
            queue = nextq
        return level
        