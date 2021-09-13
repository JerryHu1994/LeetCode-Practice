class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        edgeMap = [set() for _ in range(n)]
        dups = set()
        q = []
        for u,v in edges:
            edgeMap[u].add(v)
            edgeMap[v].add(u)
        q.append(start)
        dups.add(start)
        while len(q) > 0:
            curr = q.pop()
            if curr == end: return True
            for nextite in edgeMap[curr]:
                if nextite == end:  return True
                if nextite not in dups:
                    q.append(nextite)
                    dups.add(nextite)
        return False
            
        