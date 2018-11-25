class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        op = ["+", "-", "*", "/"]
        def cal(num1, num2, o):
            if o == "+":
                return num1+num2
            elif o == "-":
                return num1-num2
            elif o == "*":
                return num1*num2
            else:
                return num1/num2 if num2 != float(0) else float("inf")
        def helper(numlist):
            if len(numlist) == 1: return abs(numlist[0] - 24) < 1e-6
            for i in range(len(numlist)-1):
                for ope in op:
                    temp = numlist[:]
                    curr = cal(numlist[i], numlist[i+1], ope)
                    temp.pop(i)
                    temp.pop(i)
                    temp.insert(i, curr)
                    ret = helper(temp)
                    if ret: return ret
            return False
        nums = [float(n) for n in nums]
        for i in itertools.permutations(nums, len(nums)):
            ret = helper(list(i))
            if ret: return ret
        return False