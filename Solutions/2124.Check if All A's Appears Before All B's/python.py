class Solution:
    def checkString(self, s: str) -> bool:
        l = len(s)
        lasta, firstb = -1, l
        for i in range(l-1, -1, -1):
            if s[i] == "a":
                lasta = i
                break
        for i in range(l):
            if s[i] == "b":
                firstb = i
                break
        return lasta < firstb