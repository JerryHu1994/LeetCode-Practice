class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, l = [], len(part)
        for char in s:
            stack.append(char)
            if len(stack) >= l and ''.join(stack[-l:]) == part:
                stack = stack[:-l]
        return ''.join(stack)