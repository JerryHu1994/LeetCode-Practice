class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return len(nums)
        prediff = nums[1] - nums[0]
        ind, ret, currdiff = 2, 1, 0
        while ind < len(nums):
            currdiff = nums[ind] - nums[ind-1]
            print ind, currdiff, prediff
            if currdiff*prediff < 0:
                ret += 1
                prediff = currdiff
            else:
                prediff += currdiff
            ind += 1
        if currdiff != 0:   ret += 1
        return ret