class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:    return 0
        diff = abs(sum1- sum2)
        larger_num, smaller_num = (nums1, nums2) if sum1 > sum2 else (nums2, nums1)
        sorteddiff = sorted([i-1 for i in larger_num] +[6-i for i in smaller_num], reverse = True)
        currsum = 0
        for ind, val in enumerate(sorteddiff):
            if currsum + val >= diff:
                return ind + 1
            currsum += val
        return -1
        