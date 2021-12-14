class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dic = defaultdict(int)
        dic[0] = -1
        curr_sum = 0
        for ind, num in enumerate(nums):
            curr_sum += num
            dic[curr_sum] = ind
        ans = -1
        reverse = 0
        ind = len(nums)
        while True:
            if x - reverse in dic:
                pre_idx = dic[x - reverse]
                if pre_idx < ind:
                    if ans == -1:
                        ans = len(nums) - ind + pre_idx + 1
                    else:
                        ans = min(ans, len(nums) - ind + pre_idx + 1)
            ind -= 1
            if ind < 0: break
            if reverse > x: break
            reverse += nums[ind]
        return ans