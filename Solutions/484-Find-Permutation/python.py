class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        stack = [1]
        ret = []
        for i in range(len(s)):
            currnum = i+2
            if s[i] == "D":
                stack.append(currnum)
            else:
                while len(stack):
                    ret.append(stack.pop())
                stack.append(currnum)
        while len(stack):
            ret.append(stack.pop())
        return ret