class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        last = stones[-1]
        s = set(stones)
        if last ==0 or last==1:  return True
        dp = collections.defaultdict(set)
        dp[1].add(1)
        for i in stones[1:]:
            if len(dp[i]) == 0:
                continue
            else:
                if i == stones[-1]: return True
                for pre in dp[i]:
                    if pre-1 > 0 and i+pre-1 <= last and i+pre-1 in s:   dp[i+pre-1].add(pre-1)
                    if i+pre <= last and i+pre in s:   dp[i+pre].add(pre)
                    if i+pre+1 <= last and i+pre+1 in s: dp[i+pre+1].add(pre+1)
        return False