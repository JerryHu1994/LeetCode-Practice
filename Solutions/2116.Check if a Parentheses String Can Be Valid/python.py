class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1:   return False
        highend, lowend = 0, 0
        for i in range(len(s)):
            if (locked[i]) == "1":
                if s[i] == "(":
                    highend += 1
                    lowend += 1
                else:
                    highend -= 1
                    lowend -= 1
            else:
                highend += 1
                lowend -= 1
            lowend = max(lowend, 0)
            if lowend > highend:    return False
        return lowend == 0