class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ret, besttime = "", -1
        for a,b,c,d in itertools.permutations(A, 4):
            hr, mi = int(str(a)+str(b)), int(str(c)+str(d))
            if 0 <= hr <= 23 and 0 <= mi <= 59:
                if hr*24+mi > besttime:
                    hr_str = str(hr) if len(str(hr)) == 2 else "0"+str(hr)
                    mi_str = str(mi) if len(str(mi)) == 2 else "0"+str(mi)
                    ret = hr_str +":"+ mi_str
                    besttime = hr*24+mi
        return ret