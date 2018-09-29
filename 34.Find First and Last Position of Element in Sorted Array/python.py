class Solution(object):
    def helper1(self, nums, target, ind):
        l, r = 0, ind
        while l < r:
            mid = (l+r)/2
            if nums[mid] == target:
                r = mid
            else:
                l = mid + 1
        return l
    def helper2(self, nums, target, ind):
        l, r = ind, len(nums)-1
        while l < r:
            mid = (l+r)/2
            if nums[mid] == target:
                if mid==len(nums)-1 or nums[mid+1] != target:
                    return mid
                else:
                    l = mid+1
            else:
                r = mid - 1
        return l
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        found = False
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                found = True
                start = self.helper1(nums, target, mid)
                end = self.helper2(nums, target, mid)
                return [start, end]
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if not found:
            return [-1, -1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in set(nums): return [-1, -1]
        return [bisect.bisect_left(nums,target), bisect.bisect_right(nums, target)-1]