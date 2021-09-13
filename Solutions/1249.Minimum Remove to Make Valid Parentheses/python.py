class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index_to_remove = set()
        for ind, val in enumerate(s):
            if val == '(':
                stack.append((ind))
            elif val == ')':
                if len(stack) == 0:
                    index_to_remove.add(ind)
                else:
                    stack.pop()
        while len(stack) > 0:
            index_to_remove.add(stack.pop())
        ans = ""
        for ind, val in enumerate(s):
            if ind not in index_to_remove:
                ans += val
        return ans