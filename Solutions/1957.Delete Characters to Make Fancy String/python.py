class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for i in s:
            if len(res) >= 2 and res[-1] == i and res[-2] == i:
                continue
            else:
                res += i
        return res