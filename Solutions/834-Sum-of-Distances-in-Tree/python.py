class Solution(object):
        
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edgemap = collections.defaultdict(set)
        for e in edges:
            edgemap[e[0]].add(e[1])
            edgemap[e[1]].add(e[0])
        ret = [0]*N
        count = [1]*N
        
        def dfs(node, parent):
            for child in edgemap[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ret[node] += ret[child] + count[child]
        
        def dfs2(node, parent):
            for child in edgemap[node]:
                if child != parent:
                    ret[child] = ret[node] - count[child] + N - count[child]
                    dfs2(child, node)
        dfs(0, None)
        dfs2(0,None)
        return ret