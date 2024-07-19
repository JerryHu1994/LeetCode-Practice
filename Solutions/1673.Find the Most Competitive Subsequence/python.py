class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, n = [], len(nums)
        for ind, num in enumerate(nums):
            while len(stack) > 0 and stack[-1] > num and len(stack) + n-ind > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack