class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:  return []
        dp = [[] for i in range(n+1)]
        dp[0] = [""]
        dp[1] = ["0", "1", "8"]
        start = 3 if n%2==1 else 2
        for i in range(start, n+1, 2):
            for s in dp[i-2]:
                dp[i].append("1" + s + "1")
                dp[i].append("8" + s + "8")
                dp[i].append("6" + s + "9")
                dp[i].append("9" + s + "6")
                if i < n:
                    dp[i].append("0" + s + "0")
        #print dp
        return dp[n]
        
            