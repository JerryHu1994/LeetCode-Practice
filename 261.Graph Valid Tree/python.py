class Solution(object):
    def dfs(self,nodemap, visited, curr, prev):
        if visited[curr]:
            return False
        visited[curr] = True
        for i in nodemap[curr]:
            if i == prev:   continue
            if not self.dfs(nodemap, visited, i, curr):
                return False
        return True
        
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nodemap = [[] for i in range(n)]
        visited = [False]*n
        for e in edges:
            nodemap[e[0]].append(e[1])
            nodemap[e[1]].append(e[0])
        # explore from the start node
        if not self.dfs(nodemap, visited, 0, None):
            return False
        # check all nodes are visited
        for i in visited:
            if not i:   return False
        return True
        
        