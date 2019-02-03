class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s = "1"
        for i in range(n-1):
            currnum, currcount = None, None
            nexts = ""
            for i in s:
                if currnum == None:
                    currnum = i
                    currcount = 1
                elif i != currnum:
                    # append the previous
                    nexts += str(currcount) + str(currnum)
                    currnum = i
                    currcount = 1
                else:
                    currcount += 1
            nexts += str(currcount) + str(currnum)
            s = nexts
        return s