class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        for i in range(1, 10):
            if i in s1 and i in s2:
                return i
        min1, min2 = min(nums1), min(nums2)
        return min2*10+min1 if min1 >= min2 else min1*10+min2