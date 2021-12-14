class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        ans = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1] > word2[ptr2]:
                ans += word1[ptr1]
                ptr1 += 1
            elif word1[ptr1] < word2[ptr2]:
                ans += word2[ptr2]
                ptr2 += 1
            else:
                if word1[ptr1:] > word2[ptr2:]:
                    ans += word1[ptr1]
                    ptr1 += 1
                else:
                    ans += word2[ptr2]
                    ptr2 += 1
        if ptr1 < len(word1):   ans += word1[ptr1:]
        if ptr2 < len(word2):   ans += word2[ptr2:]
        return ans
    