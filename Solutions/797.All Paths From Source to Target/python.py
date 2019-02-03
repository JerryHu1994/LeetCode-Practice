class Solution(object):

    def dfs(self, dic, prevlist, ele):
        if ele == len(dic)-1:
            self.ret.append(prevlist + [ele])
            return
        for i in dic[ele]:
            self.dfs(dic, prevlist + [ele], i)
    
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        self.ret = []
        for ind, p in enumerate(graph):
            dic[ind] = p
        self.dfs(dic, [], 0)
        return self.ret