class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        curr = float("inf")
        left_min = [curr]
        for n in nums[:-1]:
            curr = min(curr, n)
            left_min.append(curr)
        curr = float("inf")
        right_min = [curr]
        for n in nums[::-1][:-1]:
            curr = min(curr, n)
            right_min.append(curr)
        right_min = right_min[::-1]
        res = float("inf")
        for i in range(1, len(nums)-1):
            if left_min[i] < nums[i] and right_min[i] < nums[i]:
                res = min(res, left_min[i] + nums[i] + right_min[i])
        return res if res != float("inf") else -1