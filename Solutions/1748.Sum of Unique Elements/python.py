class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for n in nums:  dic[n] += 1
        ans = 0
        for k,v in dic.items():
            if v == 1:  ans += k
        return ans