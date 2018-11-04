class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # check if there are nodes with multiple parents
        first, second = None, None
        p = {}
        for ind, edge in enumerate(edges):
            if edge[1] not in p:
                p[edge[1]] = edge
            else:
                first, second = p[edge[1]][:], edge[:]
                # delete the second
                edges[ind][0] = -1
                edges[ind][1] = -1
        ids = [i for i in range(2001)]
        def getid(parents, node):
            while node != parents[node]:
                node = parents[node]
            return node
        cycle = None
        for edge in edges:
            if edge[0] < 0: continue
            pa = getid(ids, edge[0])
            pb = getid(ids, edge[1])
            if pa == pb:
                return edge if first == None else first
            else:
                ids[pa] = getid(ids, ids[pb])
        return second
        
                