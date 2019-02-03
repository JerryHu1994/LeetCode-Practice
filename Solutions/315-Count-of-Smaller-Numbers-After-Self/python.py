class Solution(object):
    def merge(self, nums):
        if len(nums)==0 or len(nums)==1:
            return nums
        mid = len(nums)//2
        merge_left = self.merge(nums[:mid])
        merge_right = self.merge(nums[mid:])
        l, r = 0, 0
        ret = []
        record = 0
        while l < len(merge_left) and r < len(merge_right):
            if merge_left[l][1] <= merge_right[r][1]:
                curr = merge_left[l]
                ret.append(curr)
                self.ret[curr[0]] += record
                l += 1
            else:
                ret.append(merge_right[r])
                r += 1
                record += 1
        if l < len(merge_left):
            ret += merge_left[l:]
            for i in merge_left[l:]:    self.ret[i[0]]+=record
        if r < len(merge_right):
            ret += merge_right[r:]
        return ret
                
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.ret = [0]*len(nums)
        sort = [(i, nums[i]) for i in range(len(nums))]
        self.merge(sort)
        return self.ret