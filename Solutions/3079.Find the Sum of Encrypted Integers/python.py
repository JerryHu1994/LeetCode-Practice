class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num: int):
            numlist = [int(s) for s in str(num)]
            return int(str(max(numlist))*len(numlist))
        return sum([encrypt(val) for val in nums])