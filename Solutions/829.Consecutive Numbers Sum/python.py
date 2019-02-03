class Solution(object):
    
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        for i in range(1, int(math.sqrt(2*N))+1):
            if 2*N%i == 0:
                div = 2*N/i
                if (div-1-i)%2 == 0:
                    ret += 1
        return ret
        