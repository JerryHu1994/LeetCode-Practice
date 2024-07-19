class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 % (k*num2) == 0:
                    ans += 1
        return ans