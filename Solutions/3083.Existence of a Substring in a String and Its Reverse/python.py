class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        substringSet = set()
        reverse = s[::-1]
        for i in range(len(s)-1):
            substringSet.add(reverse[i:i+2])
        for i in range(len(s)-1):
            if s[i:i+2] in substringSet:
                return True
        return False
        