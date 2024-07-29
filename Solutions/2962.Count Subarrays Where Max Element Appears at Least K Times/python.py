class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxnum = max(nums)
        left, right, n = 0, 0, len(nums)
        ans = 0
        idx_list = []
        for ind, num in enumerate(nums):
            if num == maxnum:   idx_list.append(ind)
        ans = 0
        buffer = 0
        for startidx in range(len(nums)):
            if startidx > idx_list[buffer]:
                buffer += 1
            if len(idx_list) < k+buffer:
                break
            ans += n - idx_list[k-1+buffer]
        return ans