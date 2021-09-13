class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        for i in range(len(rungs)):
            pre = 0 if i == 0 else rungs[i-1]
            diff = rungs[i] - pre
            ans += math.ceil(diff/dist) - 1
        return ans