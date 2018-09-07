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
            