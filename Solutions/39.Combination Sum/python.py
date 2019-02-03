class Solution(object):
    
    def helper(self, candidates, target, currlist, startidx):
        if target == 0:
            self.sol.append(currlist)
            return
        for i in range(startidx, len(candidates), 1):
            if candidates[i] <= target:
                self.helper(candidates, target-candidates[i], currlist+[candidates[i]], i)
            else:
                break
        return

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.sol = []
        self.helper(candidates, target, [], 0)
        return self.sol
        