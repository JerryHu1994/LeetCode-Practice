class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)[2:]
        if b[0]=='1':
            ret = True
            for i in range(len(b)):
                if i%2==0 and b[i] != '1':
                    return False
                if i%2==1 and b[i] != '0':
                    return False
        else:
            for i in range(len(b)):
                if i%2==0 and b[i] != '0':
                    return False
                if i%2==1 and b[i] != '1':
                    return False
        return True