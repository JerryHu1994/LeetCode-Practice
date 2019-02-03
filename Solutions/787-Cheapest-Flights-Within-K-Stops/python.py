class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for f in flights:
            dic[f[0]].append(f[1:3])
        minprice = float("inf")
        queue = [[src, 0]]
        for i in range(K+1):
            nextqueue = []
            for n in queue:
                nextcities = dic[n[0]]
                for city in nextcities:
                    if city[0] == dst:  minprice = min(minprice, city[1]+n[1])
                    if city[1]+n[1] > minprice: continue
                    nextqueue.append([city[0], city[1]+n[1]])
            queue = nextqueue
        for i in queue:
            if i[0] == dst: minprice = min(i[1], minprice)
        return minprice if minprice != float("inf") else -1