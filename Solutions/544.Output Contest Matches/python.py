class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        currlist = [i for i in range(1, n+1)]
        while len(currlist) > 1:
            nextlist = []
            for i in range(len(currlist)/2):
                nextlist.append("("+str(currlist[i])+","+str(currlist[len(currlist)-1-i])+")")
            currlist = nextlist
        return currlist[0]