class Solution(object):
    def dfs(self, i, visited, moremoney, quiet):
        if visited[i]:  return
        ret = i
        visited[i] = True
        for j in moremoney[i]:
            if not visited[j]:
                self.dfs(j, visited, moremoney, quiet)
            if quiet[self.ret[j]] < quiet[ret]:
                ret = self.ret[j]
        self.ret[i] = ret
    
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        moremoney = collections.defaultdict(list)
        for pair in richer:
            moremoney[pair[1]].append(pair[0])
        visited = [False]*len(quiet)
        self.ret = [0]*len(quiet)
        for i in range(len(quiet)):
            self.dfs(i, visited, moremoney, quiet)
        return self.ret