class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_zeros, right_ones = [], []
        n = len(nums)
        curr_zero = 0
        for num in nums:
            left_zeros.append(curr_zero)
            if num == 0:    curr_zero += 1
        left_zeros.append(curr_zero)
        curr_one = 0
        right_ones.append(0)
        for num in nums[::-1]:
            if num == 1:    curr_one += 1
            right_ones.append(curr_one)
        right_ones = right_ones[::-1]
        ans = []
        curr_best = 0
        for i in range(n+1):
            curr_score = left_zeros[i] + right_ones[i]
            if curr_score > curr_best:
                ans = [i]
                curr_best = curr_score
            elif curr_score == curr_best:
                ans.append(i)
        return ans