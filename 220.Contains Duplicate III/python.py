class Solution(object):

    def getId(self, x, w):
        if x < 0:
            return (x+1)/w - 1
        else:
            return x/w
    
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:   return False
        dic = {}
        w = t+1
        for i in range(len(nums)):
            idd = self.getId(nums[i], w)
            if idd in dic:
                return True
            if idd-1 in dic and abs(nums[i] - dic[idd-1]) < w:
                return True
            if idd+1 in dic and abs(nums[i] - dic[idd+1]) < w:
                return True
            dic[idd] = nums[i]
            if i>= k:   del dic[self.getId(nums[i-k],w)]
        return False