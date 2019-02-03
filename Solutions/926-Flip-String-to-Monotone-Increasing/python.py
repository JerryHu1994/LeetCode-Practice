class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        numlist = [int(i) for i in S]
        curr, culsum = 0, []
        for i in numlist:
            curr += i
            culsum.append(curr)
        ret = culsum[-1]
        for i in range(len(S)):
            # i is the start of 1s
            if i == 0:
                ret = min(len(S)-i-culsum[-1], ret)
            else:
                ret = min(culsum[i-1] + len(S)-i-(culsum[-1]-culsum[i-1]), ret)
        return ret