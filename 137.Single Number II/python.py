class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(32):
            cnt = 0
            for j in nums:
                cnt += (j >> i) & 1
            cnt = cnt % 3
            if i == 31 and cnt == 1:
                ret -= 1 << 31
            else:
                ret |= cnt << i
        return ret