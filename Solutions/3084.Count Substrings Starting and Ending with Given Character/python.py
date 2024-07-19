class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        prefix = [0]
        currsum = 0
        for char in s[:-1]:
            if char == c:   currsum += 1
            prefix.append(currsum)
        postfix = [0]
        currsum = 0
        for char in s[::-1][:-1]:
            if char == c:   currsum += 1
            postfix.append(currsum)
        postfix = postfix[::-1]
        res = 0
        count = 0
        for i, char in enumerate(s):
            if char == c:
                count += 1
                res += prefix[i] + postfix[i]
        return int(res/2)+count