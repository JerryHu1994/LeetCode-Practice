class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (high+low)//2
            count = 0
            j = 0
            for i in range(len(nums)):
                # found the index exactly smaller than nums[i]+mid
                rightidx = bisect.bisect_right(nums, nums[i]+mid) 
                count += rightidx - i - 1
            if count < k:
                # included too little, make threshold larger
                low = mid + 1
            else:
                high = mid
        return low