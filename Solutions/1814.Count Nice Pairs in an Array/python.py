class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            rev = int(str(num)[::-1])
            dic[num - rev] += 1
        ans = 0
        for k, v in dic.items():
            ans += int((v-1)*v//2) % 1000000007
        return ans % 1000000007