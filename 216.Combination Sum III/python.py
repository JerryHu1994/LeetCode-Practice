class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def helper(prelist, start):
            if sum(prelist) == n and len(prelist) == k:
                ans.append(prelist)
                return
            if len(prelist) >= k or start > 9:  return
            for i in range(start, 10):
                helper(prelist+[i], i+1)
        helper([], 1)
        return ans