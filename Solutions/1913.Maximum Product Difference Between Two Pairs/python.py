class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)
        hitsmall, hitlarge = False, False
        remain = []
        for n in nums:
            if not hitsmall and n == smallest:
                hitsmall = True
            elif not hitlarge and n == largest:
                hitlarge = True
            else:
                remain.append(n)
        return largest*max(remain) - smallest*min(remain)