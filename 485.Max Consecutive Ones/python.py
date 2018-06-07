class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, currlen = 0, 0
        for i in nums:
            if i == 1:
                currlen += 1
            else:
                if currlen > ret:
                    ret = currlen
                currlen = 0
        if currlen > ret:   ret = currlen
        return ret
        