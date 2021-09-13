class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        dic = {}
        for ind, char in enumerate(s):
            if char in dic:
                ans = max(ind - dic[char] - 1, ans)
            else:
                dic[char] = ind
        return ans
                