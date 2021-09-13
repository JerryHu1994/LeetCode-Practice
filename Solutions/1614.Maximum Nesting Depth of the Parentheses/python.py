class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        ans = 0
        for char in s:
            if char == "(":
                curr += 1
                ans = max(ans, curr)
            elif char == ")":
                curr -= 1
        return ans