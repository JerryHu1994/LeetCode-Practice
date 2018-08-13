class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:    return []
        ret = []
        currstart, prev = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if prev == currstart:
                    ret.append(str(prev))
                else:
                    ret.append(str(currstart)+"->"+str(prev))
                currstart = prev = nums[i]
            else:
                prev+=1
        if prev == currstart:
            ret.append(str(prev))
        else:
            ret.append(str(currstart)+"->"+str(prev))
        return ret