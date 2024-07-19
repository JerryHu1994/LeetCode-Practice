class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 1
        left, right, n = 0, 0, len(nums)
        currmin, currmax = nums[0], nums[0]
        cnt = 0
        dic = defaultdict(int)
        ans = 0
        while right < n:
            li = list(dic.keys())
            if len(li) > 0:
                currmin, currmax = min(li), max(li)
                if nums[right] > currmin+2 or nums[right] < currmax-2:
                    cnt -= 1
                    dic[nums[left]] -= 1
                    if dic[nums[left]] == 0:    del dic[nums[left]]
                    left += 1
                    continue
            dic[nums[right]] += 1
            cnt += 1
            ans += cnt
            right += 1
        return ans