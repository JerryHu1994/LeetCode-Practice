class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in nums:  xor ^= i
        diffbit = 1
        while diffbit & xor == 0:   diffbit = diffbit << 1
        num1, num2 = 0, 0
        for n in nums:
            if n & diffbit == 0:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]