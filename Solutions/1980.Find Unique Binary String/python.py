class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        visited = set(nums)
        n = len(nums[0])
        li = ["1", "0"]
        def backtrack(li, n):
            if n == 0:
                return li
            nextli = []
            for element in li:
                nextli.append(element+"0")
                nextli.append(element+"1")
            return backtrack(nextli, n-1)
        finallist = backtrack(li, n-1)
        for s in finallist:
            if s not in visited:  return s