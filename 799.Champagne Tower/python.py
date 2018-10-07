class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if query_row == 0:
            return 1.0 if poured >= 1 else poured
        dp = [[] for i in range(query_row+1)]
        dp[0].append(0.0 if poured <= 1 else float(poured-1))
        for i in range(1, query_row+1):
            dp[i-1].insert(0, 0.0)
            dp[i-1].append(0.0)
            if i == query_row:
                pre = dp[i-1][query_glass]/2 + dp[i-1][query_glass+1]/2
                return 1.0 if pre >= 1 else pre
            for j in range(i+1):
                pre = dp[i-1][j]/2 + dp[i-1][j+1]/2
                dp[i].append(0 if pre <= 1 else pre-1)