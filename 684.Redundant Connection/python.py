class Solution(object):
    def dfs(self, node1, node2):
        visited = set([node1])
        stack = [node1]
        while stack:
            curr = stack.pop()
            if curr == node2:   return True
            neighbors = self.dic[curr]
            for n in neighbors:
                if n not in visited:    
                    stack.append(n)
                    visited.add(n)
        return False
        
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.dic = collections.defaultdict(set)
        for e in edges:
            node1, node2 = e
            if node1 in self.dic and node2 in self.dic and self.dfs(node1, node2):
                return e
            self.dic[node1].add(node2)
            self.dic[node2].add(node1)
            
class DSU:
    def __init__(self):
        self.parents = [i for i in range(1001)]
        self.ranks = [0]*1001
        
    # outputs a unique id for x with path compression
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    # connects x and y together with union-by-rank
    def union(self, x, y):
        xid, yid = self.find(x), self.find(y)
        if xid == yid: # duplicate edge
            return False
        elif self.ranks[xid] < self.ranks[yid]:
            self.parents[xid] = yid
        elif self.ranks[xid] > self.ranks[yid]:
            self.parents[yid] = xid
        else:
            self.parents[yid] = xid
            self.ranks[xid] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        for e in edges:
            if not dsu.union(e[0], e[1]):
                return e