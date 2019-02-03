class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sortnums, ret, l = sorted(nums), 0, len(nums)
        for i in range(l-2):
            currcount = 0
            left, right = i+1, l-1
            while left<right:
                if sortnums[left] + sortnums[right] >= target-sortnums[i]:
                    right -= 1
                else:
                    currcount += right-left
                    left += 1
            ret += currcount
        return ret