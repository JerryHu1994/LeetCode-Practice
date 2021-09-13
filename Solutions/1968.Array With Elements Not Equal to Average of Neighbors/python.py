class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [0 for i in range(len(nums))]
        i, j, curr = 0, len(nums)-1, 0
        while curr < len(nums):
            if curr%2 == 0:
                ans[curr] = nums[j]
                j -= 1
            else:
                ans[curr] = nums[i]
                i += 1
            curr += 1
        return ans