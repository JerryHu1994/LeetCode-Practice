class Solution(object):
    
    def helper(self, candidates, target, currlist, startidx):
        if target == 0:
            self.sol.append(currlist)
            return True
        s = startidx
        ret = False
        while s < len(candidates):
            if candidates[s] <= target:
                # jump to the next different value if true
                if self.helper(candidates, target-candidates[s], currlist+[candidates[s]], s+1):
                    ret = True
                    currval = candidates[s]
                    s+=1
                    while s<len(candidates) and candidates[s] == currval:
                        s+=1
                else:
                    s+=1
            else:
                break
            
        return ret
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.sol = []
        self.helper(candidates, target, [], 0)
        return self.sol