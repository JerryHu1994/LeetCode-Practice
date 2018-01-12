class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sortedlist, bestdiff, ret = sorted(nums), None, 0
        for ind, val in enumerate(sortedlist):
            left, right = ind+1, len(sortedlist)-1
            while left < right:
                currsum = val + sortedlist[left] + sortedlist[right]
                currdiff = currsum - target
                if currdiff == 0:
                    return currsum
                elif currdiff < 0:
                    left+=1
                else:
                    right-=1
                if bestdiff==None or abs(currdiff)<bestdiff:
                    bestdiff = abs(currdiff)
                    ret = currsum
        return ret
            