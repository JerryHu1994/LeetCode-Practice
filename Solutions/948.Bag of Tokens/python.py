class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        l = len(tokens)
        tokens = sorted(tokens)
        left, right = 0, l-1
        ret = 0
        currpoints = 0
        done = True
        while done and left <= right:
            done = False
            # trade power for points as much as possible
            while left <= right and tokens[left] <= P:
                P -= tokens[left]
                left += 1
                currpoints += 1
            # update answer
            ret = max(ret, currpoints)
            # trade one point for power
            if left <= right and currpoints > 0:
                currpoints -= 1
                P += tokens[right]
                right -= 1
                done = True
        return ret