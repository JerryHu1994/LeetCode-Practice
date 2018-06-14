class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ret = [0]*len(temperatures)
        q = []
        heapq.heappush(q, (temperatures[0], 0))
        for i in range(1, len(temperatures)):
            if len(q) == 0:
                heapq.heappush(q, (temperatures[i], i))
                continue
            while True:
                if len(q) == 0: break
                curr = heapq.heappop(q)
                if curr[0] < temperatures[i]:
                    #update for a warmer temperature
                    ret[curr[1]] = i - curr[1]
                else:
                    heapq.heappush(q, curr)
                    break
            heapq.heappush(q, (temperatures[i], i))
        return ret