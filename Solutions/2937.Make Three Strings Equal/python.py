class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        idx = 0
        while idx < len(s1) and idx < len(s2) and idx < len(s3) and s1[idx] == s2[idx] and s2[idx] == s3[idx]:
            idx += 1
        return -1 if idx == 0 else len(s1) + len(s2) + len(s3) - idx*3