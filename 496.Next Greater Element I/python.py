class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, dic = [], {}
        for i in nums:
            if len(stack) == 0:
                stack.append(i)
            else:
                while len(stack) != 0 and i > stack[-1]:
                    last = stack.pop()
                    dic[last] = i
                stack.append(i)
        ret = []
        for i in findNums:
            if i in dic:
                ret.append(dic[i])
            else:
                ret.append(-1)
        return ret
                