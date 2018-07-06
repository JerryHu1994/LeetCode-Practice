class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        if n < 0:  return ret
        ret.append(0)
        if n==0:    return ret
        addon = 1
        for i in range(1,n+1):
            curr_size = len(ret)
            for i in range(curr_size-1, -1, -1):
                ret.append(ret[i] + addon)
            addon = addon << 1
        return ret
        