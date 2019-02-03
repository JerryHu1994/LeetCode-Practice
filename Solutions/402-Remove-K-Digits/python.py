class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k==0:    return num
        if len(num) <= k:    return "0"
        stack = []
        for i in num:
            while len(stack) and k > 0 and stack[-1] > int(i):
                stack.pop()
                k -= 1
            stack.append(int(i))
        while k > 0:
            stack.pop()
            k -= 1
        return "".join([str(i) for i in stack]).lstrip("0") or "0"