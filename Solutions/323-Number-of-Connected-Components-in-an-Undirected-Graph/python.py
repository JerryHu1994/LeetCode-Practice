class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = {}
        for i in range(n):
            dic[i] = set()
        for e in edges:
            dic[e[0]].add(e[1])
            dic[e[1]].add(e[0])
        cnt = 0
        while len(dic):
            start = sorted(dic.items())[0][0]
            li = [start]
            while len(li):
                curr = li.pop(0)
                if curr in dic:
                    li+=dic[curr]
                    del dic[curr]
            cnt += 1
        return cnt