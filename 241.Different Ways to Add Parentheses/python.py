class Solution(object):
    def helper(self, input):
        flag = True
        ret = []
        for ind,val in enumerate(input):
            if val in "+-*":
                flag = False
                left = self.helper(input[:ind])
                right = self.helper(input[ind+1:])
                for i in left:
                    for j in right:
                        res = 0
                        if val == "+":
                            res = i+j
                        elif val == "-":
                            res = i-j
                        else:
                            res = i*j
                        ret.append(res)
        if flag:
            return [int(input)]
        else:
            return ret
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input)
                