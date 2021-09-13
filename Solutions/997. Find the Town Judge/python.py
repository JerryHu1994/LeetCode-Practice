class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        remain = set([i for i in range(1, N+1)])
        for fro, to in trust:
            if fro in remain:    remain.remove(fro)
            graph[to].add(fro)
        ans = []
        for remain_ele in remain:
            if len(graph[remain_ele]) == N-1:
                ans.append(remain_ele)
        return ans[0] if len(ans) == 1 else -1