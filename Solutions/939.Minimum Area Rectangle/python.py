class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sort = collections.defaultdict(list)
        for p in points:    sort[p[1]].append(p)
        keys = sorted(sort.keys())
        dic = {}
        ret = float("inf")
        for k in keys:
            currpoints = sort[k]
            sortedy = sorted([p[0] for p in currpoints])
            l = len(currpoints)
            for currpair in itertools.combinations(sortedy, 2):
                if currpair in dic:
                    ret = min(ret, abs(currpair[0]-currpair[1])*(k-dic[currpair]))
                dic[currpair] = k
        return ret if ret != float("inf") else 0