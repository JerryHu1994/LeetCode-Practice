class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = -1, -1
        currsum, ret = 0, float("inf")
        while True:
            if currsum < s:
                # move right
                right += 1
                if right>= len(nums): break
                currsum += nums[right]
            else:
                # move left
                left += 1
                currsum -= nums[left]
            if currsum >= s:
                ret = min(right-left, ret)
        
        return 0 if ret == float("inf") else ret