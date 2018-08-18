class Solution(object):
    def helper(self, piles, K):
        return sum([(i-1)//K+1 for i in piles])
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        low, high = 1, max(piles)
        while low < high:
            mid = (low+high)//2
            currhour = self.helper(piles, mid)
            if currhour <= H:
                high = mid
            else:
                low = mid+1
        return low