class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortnums, ret, l = sorted(nums), [], len(nums)
        for ind, val in enumerate(sortnums):
            if ind > 0 and sortnums[ind] == sortnums[ind-1]:    continue
            left, right = ind+1, l-1
            while left<right:
                s = sortnums[left] + sortnums[right] + val
                if s > 0:
                    right-=1
                elif s < 0:
                    left+=1
                else:
                    ret.append([val, sortnums[left], sortnums[right]])
                    left+=1
                    right-=1
                    while left >=0 and left < l and sortnums[left-1]==sortnums[left]:
                        left+=1
                    while right >=0 and right < l and sortnums[right+1]==sortnums[right]:
                        right-=1
        return ret
                