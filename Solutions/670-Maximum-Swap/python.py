class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numlist = [int(i) for i in str(num)]
        idxlist = [None]*10
        for i in range(len(numlist)-1, -1, -1):
            if idxlist[numlist[i]] == None:
                idxlist[numlist[i]] = i
        for i in range(len(numlist)-1):
            for j in range(9, numlist[i], -1):
                if idxlist[j] != None and idxlist[j] > i:
                    numlist[i], numlist[idxlist[j]] = j, numlist[i]
                    return int("".join([str(i) for i in numlist]))
        return num