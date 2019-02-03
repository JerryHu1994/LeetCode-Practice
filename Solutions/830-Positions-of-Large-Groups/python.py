class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        left, right  = 0, 1
        while right < len(S):
            currcount = 1
            while right < len(S) and S[right] == S[right-1]:
                currcount += 1
                right += 1
            if currcount >= 3:
                ret.append([left, right-1])
            left, right = right, right+1
        return ret