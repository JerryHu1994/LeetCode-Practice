class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while len(pushed) and len(popped):
            if len(stack) == 0 or popped[0] != stack[-1]:
                stack.append(pushed.pop(0))
            else:
                popped.pop(0)
                stack.pop()
        for ind, num in enumerate(stack[::-1]):
            if num != popped[ind]:  return False
        return True