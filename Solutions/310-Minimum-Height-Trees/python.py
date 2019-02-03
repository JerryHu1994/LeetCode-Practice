class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:  return [0]
        dic = collections.defaultdict(list)
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
        degrees = [len(dic[i]) for i in range(n)]
        ones = [i for i in range(n) if degrees[i] == 1]
        ret = []
        while ones:
            temp = []
            ret = ones[:]
            for o in ones:
                for n in dic[o]:
                    degrees[n] -= 1
                    if degrees[n] == 1:
                        temp.append(n)
            ones = temp
        return ret