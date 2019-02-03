wclass Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        def helper(d):
            cnt = 0
            for i in range(len(stations)-1):
                cnt += int(math.floor((float(stations[i+1])-float(stations[i]))/d))
            return cnt <= K
        low, high = float(0.0), float(stations[-1]-stations[0])
        while high - low > 10**(-6):
            mid = (float(high)+float(low))/2.0
            if helper(mid):
                high = mid
            else:
                low = mid
        return low