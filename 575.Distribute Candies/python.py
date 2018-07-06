class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        half = len(candies)/2
        s = set(candies)
        if len(s) >= half:
            return half
        else:
            return len(s)