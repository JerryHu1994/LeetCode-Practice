class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = sorted(list(set(nums)))
        left = lower
        curr = 0
        ret = []
        while curr < len(nums):
            if nums[curr] != left:
                # add the missing range for [left, nums[curr]-1]
                if left == nums[curr]-1:
                    ret.append(str(left))
                else:
                    ret.append(str(left)+"->"+str(nums[curr]-1))
                left = nums[curr]
            else:
                left += 1
                curr += 1
        if left <= upper:
            ret.append(str(left) if left == upper else str(left)+"->"+str(upper))
        return ret