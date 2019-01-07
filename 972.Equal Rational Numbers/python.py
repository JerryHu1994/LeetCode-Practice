class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        from fractions import Fraction
        def helper(num):
            if "." not in num:
                return Fraction(int(num), 1)
            i = num.index(".")
            ans = Fraction(int(num[:i]), 1)
            num = num[i+1:]
            # no repeating ending
            if "(" not in num:
                if num:
                    ans += Fraction(int(num), 10**len(num))
                return ans
            i = num.index("(")
            if i:
                ans += Fraction(int(num[:i]), 10**i)
            num = num[i+1:-1]
            j = len(num)
            ans += Fraction(int(num), 10**i*(10**j-1))
            return ans
            
        return helper(S) == helper(T)