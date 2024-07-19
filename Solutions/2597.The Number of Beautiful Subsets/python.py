class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0
        def helper(currlist:List[int], cnt:defaultdict, next_nums:List[int]):
            if len(currlist) > 0:
                self.ans += 1
            if len(next_nums) == 0:
                return
            for ind, num in enumerate(next_nums):
                if cnt[num-k] == 0 and cnt[num+k] == 0:
                    cnt[num] += 1
                    helper(currlist+[num], cnt, next_nums[ind+1:])
                    cnt[num] -= 1
        helper([], defaultdict(int), nums)
        return self.ans
