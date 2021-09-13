class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if len(stack) > 0:
                (lastelement, lastcount) = stack[-1]
                if lastelement == i:
                    if lastcount == k-1:
                        stack = stack[:1-k]
                    else:
                        stack.append((i, lastcount + 1))
                else:
                    stack.append((i, 1))
            else:
                stack.append((i, 1))
        return "".join([t[0] for t in stack])