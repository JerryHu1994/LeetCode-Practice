class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = defaultdict(int)
        for num in arr:
            if num-difference not in dic:
                dic[num] = 1
            else:
                dic[num] = dic[num-difference]+1
        ans = 0
        for val in dic.values():
            ans = max(ans, val)
        return ans