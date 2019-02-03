class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:  return 0
        magical = [1, 2, 2]
        if n <= 3:   return 1
        currnum, occ_ptr, ret = 1, 2, 1
        while len(magical) < n:
            print magical[occ_ptr]
            if currnum == 1:
                ret += magical[occ_ptr]
            magical += [currnum]*magical[occ_ptr]
            occ_ptr += 1
            if currnum == 1:
                currnum = 2
            elif currnum == 2:
                currnum = 1
        if len(magical) != n:
            if magical[-1] == 1:
                return ret-1
        return ret