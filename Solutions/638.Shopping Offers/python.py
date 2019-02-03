class Solution(object):
    def helper(self, price, special, needs):
        ret = sum([price[i]*needs[i]    for i in range(len(price))])
        for sp in special:
            newneed = needs[:]
            good = True
            for ind, num in enumerate(sp[:-1]):
                newneed[ind] -= num
                if newneed[ind] < 0:
                    good = False
                    break
            if good:
                ret = min(ret, sp[-1] + self.helper(price, special, newneed))
        return ret
            
        
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """ 
        return self.helper(price, special, needs)
        