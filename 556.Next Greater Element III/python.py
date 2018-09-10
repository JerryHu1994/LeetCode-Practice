class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        numlist = [int(i) for i in str(n)]
        currlist, currmax = [], -float("inf")
        for i in range(len(numlist)-1, -1, -1):
            val = numlist[i]
            print val
            if val < currmax:
                # swap could happen
                sortedlist = sorted(currlist)
                ind = bisect.bisect_right(sortedlist, val)
                swap = sortedlist[ind]
                sortedlist[ind], numlist[i] = val, swap
                ret = int("".join([str(i) for i in numlist[:i+1]+sortedlist]))
                return -1 if ret > 2** 31 -1 else ret
            else:
                currmax = max(currmax, val)
                currlist.append(val)
        return -1