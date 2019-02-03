class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dic = collections.defaultdict(list)
        self.ret = None
        for t in tickets:   dic[t[0]].append(t[1])
        def dfs(pre):
            curr = pre[-1]
            if len(dic) == 0:
                if self.ret == None:
                    self.ret = pre
                    return True
            if curr not in dic: return 
            currs = sorted(dic[curr])
            for n in currs:
                # pick n as next
                dic[curr].remove(n)
                if len(dic[curr]) == 0: del dic[curr]
                if dfs(pre+[n]):    return True
                dic[curr].append(n)
        dfs(["JFK"])
        return self.ret