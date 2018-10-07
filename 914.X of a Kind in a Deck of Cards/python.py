class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        cnt = collections.Counter(deck)
        vals = [v for v in cnt.values()]
        minval = min(vals)
        factors = [i for i in range(2, minval+1) if minval%i == 0]
        for f in factors:
            valid = True
            for v in vals:
                if v%f != 0:
                    valid = False
                    break
            if valid:   return True
        return False