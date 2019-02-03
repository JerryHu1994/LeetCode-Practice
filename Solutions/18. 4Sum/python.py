class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sortnums, ret, l = sorted(nums), [], len(nums)
        s = set()
        for i in range(l):
            for j in range(i+1,l):
                left, right = j+1, l-1
                while left<right:
                    currsum = sortnums[left] + sortnums[right] + sortnums[i] + sortnums[j] - target
                    if currsum > 0:
                        right-=1
                    elif currsum < 0:
                        left+=1
                    else:
                        currset = (sortnums[i], sortnums[j], sortnums[left], sortnums[right])
                        if currset not in s:   s.add(currset)
                        left+=1
                        right-=1
                        while left<right and sortnums[left-1]==sortnums[left]:   left+=1
                        while left<right and sortnums[right+1]==sortnums[right]:   right-=1
        return [list(i) for i in s]