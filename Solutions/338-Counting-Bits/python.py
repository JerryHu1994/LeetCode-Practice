class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nums = [0]*(num+1)
        nums[0] = 0
        if num == 0:    return nums
        nums[1] = 1
        idx = 2
        b = 2
        while True:
            end = False
            for i in range(b):
                if idx > num:
                    end = True
                    break
                nums[idx] = nums[idx-b] + 1
                idx += 1
            b = b << 1
            if end: break
        return nums