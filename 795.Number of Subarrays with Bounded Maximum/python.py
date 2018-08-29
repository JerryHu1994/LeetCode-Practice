class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        globallist, prev, ret = [], 0, 0
        for i in range(len(A)):
            if A[i] > R:
                # got an invalid, save
                globallist.append(A[prev:i])
                prev = i+1
        globallist.append(A[prev:]) #append the last one
        for currlist in globallist:
            currvalid = None
            for ind, val in enumerate(currlist):
                if L <= val <= R:
                    # the current value is valid
                    ret += ind + 1
                    currvalid = ind
                else:
                    # the current valid is invalid
                    if currvalid != None:   ret += currvalid+1
        return ret
                