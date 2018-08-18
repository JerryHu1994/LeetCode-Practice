class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binnum = bin(N)[2:]
        lastone = None
        ret = 0
        for i in range(len(binnum)):
            if binnum[i] == "1":
                if lastone != None:
                    ret = max(ret, i - lastone)
                    lastone = i
                else:
                    lastone = i
        return ret