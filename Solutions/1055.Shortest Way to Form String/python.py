class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char_set = set([c for c in source])
        ans = 0
        leftptr, rightptr = 0, 0
        while rightptr < len(target):
            while leftptr < len(source) and rightptr < len(target):
                if target[rightptr] not in char_set:    return -1
                if source[leftptr] == target[rightptr]:
                    rightptr += 1
                leftptr += 1
            if leftptr == len(source):
                leftptr = 0
            ans += 1
        return ans