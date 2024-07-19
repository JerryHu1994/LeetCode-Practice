class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        left, right = 0, 0
        res = 0
        currlist = defaultdict(int)
        while left < len(nums):
            while right < len(nums) and len(currlist) < distinct_count:
                currlist[nums[right]] += 1
                right += 1
            if len(currlist) == distinct_count:
                res += len(nums) + 1 - right
            currlist[nums[left]] -= 1
            if (currlist[nums[left]]) == 0: del currlist[nums[left]]
            left += 1
        return res