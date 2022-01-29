class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        s = set(nums)
        ans = []
        for num in s:
            if cnt[num] == 1 and num-1 not in cnt and num+1 not in cnt:
                ans.append(num)
        return ans