class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numlist = ""
        for char in s:
            num = ord(char) - ord('a') + 1
            numlist += str(num)
        for i in range(k):
            currsum = 0
            for val in numlist:
                currsum += int(val)
            numlist = str(currsum)
        return int(numlist)