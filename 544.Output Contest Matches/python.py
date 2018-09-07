class Solution(object):
    def helper(self, li):
        if len(li) == 1:
            return str(li[0])
        middle = ",".join([self.helper(i) for i in li])
        return "(" + middle + ")"
        
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        currlist = [[i+1] for i in range(n)]
        while len(currlist) != 2:
            nextlist = []
            for i in range(0, len(currlist)/2):
                nextlist.append([currlist[i]] + [currlist[len(currlist)-1-i]])
            currlist = nextlist
        ret = self.helper(currlist)
        return ret