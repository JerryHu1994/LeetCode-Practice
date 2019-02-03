# solution 1
class Solution(object):
    # return True if maximum average is above mid
    # return False if maximum average is below mid
    def helper(self, nums, mid, k):
        reduced_array = [i-mid for i in nums]
        currsum = sum(reduced_array[0:k])
        if currsum >=0: return True
        total_sum, prev_sum, min_prev = currsum, 0, 0
        for i in range(k, len(nums)):
            total_sum += reduced_array[i]
            prev_sum += reduced_array[i-k]
            min_prev = min(min_prev, prev_sum)
            if total_sum - min_prev >=0:
                return True
        return False
        
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        nums = [float(i) for i in nums]
        max_val, min_val = max(nums), min(nums)
        lastmid = float('-inf')
        while True:
            mid = (max_val + min_val)/2
            if self.helper(nums, mid, k):
                # mid is too small
                min_val = mid
            else:
                # mid is too large
                max_val = mid
            if abs(mid - lastmid) < 0.00001:
                return mid
            lastmid = mid
            #print mid
        return None
            
# solution 2
import numpy as np

class Solution(object):
    def findMaxAverage(self, nums, k):
        lo, hi = min(nums), max(nums)
        nums = np.array([0] + nums)
        while hi - lo > 1e-5:
            mid = nums[0] = (lo + hi) / 2.
            sums = (nums - mid).cumsum()
            mins = np.minimum.accumulate(sums)
            if (sums[k:] - mins[:-k]).max() > 0:
                lo = mid
            else:
                hi = mid
        return lo