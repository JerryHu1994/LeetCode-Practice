class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = num1[::-1], num2[::-1]
        total_len = len(n1) + len(n2)
        result = [0]*total_len
        for ind2, val2 in enumerate(n2):
            for ind1, val1 in enumerate(n1):
                result[ind2 + ind1] += int(val2)*int(val1)
        carry = 0
        for ind, val in enumerate(result):
            div = (carry + val)//10
            remain = (carry + val)%10
            carry = div
            result[ind] = remain
        fliped = result[::-1]
        while fliped[0] == 0 and len(fliped)>1:
            del fliped[0]
        str_arr = [str(i) for i in fliped]
        return "".join(str_arr)