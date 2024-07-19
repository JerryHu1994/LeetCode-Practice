class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = ["1", "0"]
        for i in range(n-1):
            nextlist = []
            for num in ans:
                if num[-1] == "1":
                    nextlist.append(num+"0")
                nextlist.append(num+"1")
            ans = nextlist
        return ans