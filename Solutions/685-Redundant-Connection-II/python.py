class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # check if there are nodes with multiple parents
        # check if there are nodes with multiple parents
        first, second = None, None
        graph = {}
        for ind, edge in enumerate(edges):
            if edge[1] not in graph:
                graph[edge[1]] = edge
            else:
                # save the invalid and terminate
                first, second = graph[edge[1]], edge
                edges.pop(ind)
                break
        parents = [i for i in range(2000)]
        def getParent(num):
            while parents[num] != num:
                num = parents[num]
            return num
        for e in edges:
            pa, pb = getParent(e[0]), getParent(e[1])
            # 如果
            if pa == pb:
                return e if first == None else first
            else:
                parents[pa] = getParent(pb)
        return second
        
                