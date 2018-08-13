class Solution(object):
    def dfs(self, graph, ind, color):
        if color[ind] > 0: return color[ind] == 2
        color[ind] = 1 #set to visited in current dfs
        for i in graph[ind]:
            if color[i] == 2:   continue
            # found a node visited in current dfs, or dfs returns False => found a cycle
            if color[i] == 1 or not self.dfs(graph, i, color):
                return False
        # didn't find any cycle, set to already visited
        color[ind] = 2
        return True
    
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        l = len(graph)
        color = [0]*l # 0 for never visited, 1 for currently visited in dfs, 2 for already visited
        ret = []
        for i in range(l):
            if self.dfs(graph, i, color):
                ret.append(i)
        return ret
        