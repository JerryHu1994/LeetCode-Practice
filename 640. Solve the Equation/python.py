class Solution(object):
    def helper(self, equ):
        factor, constant, i, currsign = 0, 0, 0, 1
        while i < len(equ):
            if equ[i] == "+":
                currsign = 1
                i += 1
            elif equ[i] == "-":
                currsign = -1
                i += 1
            elif equ[i] == "x":
                factor += currsign
                i += 1
            else:
                num, j = "", i
                while j < len(equ) and equ[j].isdigit():
                    num += equ[j]
                    j += 1
                i = j
                if i>= len(equ) or equ[i] != "x":
                    constant += currsign*int(num)
                else:
                    factor += currsign*int(num)
                    i += 1
        return factor, constant
    
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equalidx = equation.index("=")
        leftfac, leftcons = self.helper(equation[:equalidx])
        rightfac, rightcons = self.helper(equation[equalidx+1:])
        fac, const = leftfac - rightfac, rightcons - leftcons
        if fac == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x="+str(const/fac)