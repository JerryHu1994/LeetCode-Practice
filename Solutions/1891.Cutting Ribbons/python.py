class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        ribbons.sort()
        def isPossible(ribbons, k, seglen):
            count = 0
            for rib in ribbons:
                count += (rib//seglen)
                if count >= k:  return True
            return False
        left, right = 1, ribbons[-1]
        if isPossible(ribbons, k, right):   return right
        while left < right:
            mid = (left+right)//2
            if (isPossible(ribbons, k, mid)):
                left = mid+1
            else:
                right = mid
        return left-1
        
        