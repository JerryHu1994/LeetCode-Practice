class Solution:
    def minimumMoves(self, s: str) -> int:
        ind = 0
        ans = 0
        while ind < len(s):
            if s[ind] == "O":
                ind += 1
            else:
                ind += 3
                ans += 1
        return ans