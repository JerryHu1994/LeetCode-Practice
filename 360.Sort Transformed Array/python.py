class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            if b > 0:
                return [a*pow(i,2)+b*i+c for i in nums]
            else:
                return [a*pow(i,2)+b*i+c for i in nums][::-1]
        
        ret = []
        mid = -float(b)/(2*float(a))
        left, right = 0, len(nums)-1
        while left <= right:
            print mid, nums[left], nums[right]
            if abs(mid-nums[left]) > abs(nums[right]-mid):
                ret.append(a*pow(nums[left],2)+b*nums[left]+c)
                left += 1
            else:
                ret.append(a*pow(nums[right],2)+b*nums[right]+c)
                right -= 1
        if a > 0:
            return ret[::-1]
        else:
            return ret
        