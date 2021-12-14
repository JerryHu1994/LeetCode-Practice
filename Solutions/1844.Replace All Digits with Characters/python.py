class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(0,len(s),2):
            res += s[i]
            if i == len(s) - 1: break
            res += chr(ord(s[i])+int(s[i+1]))
        return res