class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        numlist = []
        carry = 0
        n1, n2, l = num1[::-1], num2[::-1], max(l1, l2)
        for i in range(l):
            add1 = n1[i] if i < l1 else 0
            add2 = n2[i] if i < l2 else 0
            currnum = int(add1) + int(add2) + carry
            if currnum > 10:
                currnum -= 10
                carry = 1
            else:
                carry = 0
            numlist.append(currnum)
        if carry == 1:  numlist.append(carry)
        ret = 0
        for i in range(len(numlist)):
            ret += numlist[i]*(10**i)
        return str(ret)