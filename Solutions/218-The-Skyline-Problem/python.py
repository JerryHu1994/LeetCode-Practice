class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = [(l, -h, r)  for l, r, h in buildings] + [(r, 0, float("inf"))   for l, r, h in buildings] # 1 for entering, -1 for leaving
        events.sort()
        res = [[0, 0]] # start with origin
        hq = [(0, float("inf"))] # (where initial skyline starts, when it ends)
        for l, neg_h, r in events:
            while l >= hq[0][1]:
                heapq.heappop(hq)
            if neg_h:#if it starts the skyline, append it
                heapq.heappush(hq, (neg_h, r))
            if res[-1][1] != -hq[0][0]:
                res.append([l, -hq[0][0]])
        return res[1:]