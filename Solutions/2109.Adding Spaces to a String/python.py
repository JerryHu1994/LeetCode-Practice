class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        prev = 0
        for ind,num in enumerate(spaces):
            res += s[prev:num]
            prev = num
            res += " "
        if prev <= len(s)-1:
            res += s[prev:]
        return res