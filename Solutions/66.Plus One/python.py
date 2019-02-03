class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ptr = len(digits)-1
        carry = 1
        while ptr >= 0:
            if digits[ptr] == 9 and carry == 1:
                digits[ptr] = 0
                carry = 1
            else:
                digits[ptr] += 1
                return digits
            ptr -= 1
        
        if carry==1:
            digits.insert(0, 1)
        return digits