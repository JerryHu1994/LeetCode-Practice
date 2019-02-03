class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0]*len(T)
        for ind, val in enumerate(T):
            if len(stack) == 0:
                stack.append((val, ind))
                continue
            else:
                while len(stack) and stack[-1][0] < val:
                    temp, index = stack.pop()
                    ret[index] = ind - index
                stack.append((val, ind))
        return ret