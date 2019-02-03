class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        preseat = None
        dis = [float("inf")]*len(seats)
        for ind, val in enumerate(seats):
            if val == 1:
                preseat = ind
            else:
                if preseat != None:
                    dis[ind] = ind - preseat
        ret = 0
        preseat = None
        for ind in range(len(seats)-1, -1, -1):
            val = seats[ind]
            if val == 1:
                preseat = ind
            else:
                if preseat != None:
                    dis[ind] = min(dis[ind], preseat - ind)
                ret = max(ret, dis[ind])
        return ret