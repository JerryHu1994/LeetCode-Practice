class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses, heaters, ret = sorted(houses), sorted(heaters), 0
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            dis = 0
            if pos == 0:
                dis = heaters[0] - house
            elif pos == len(heaters):
                dis = house - heaters[-1]
            else:
                dis = min(house - heaters[pos-1], heaters[pos] - house)
            ret = max(ret, dis)
        return ret
                