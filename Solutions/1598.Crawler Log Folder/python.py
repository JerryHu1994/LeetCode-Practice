class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for op in logs:
            if op == "../":
                if len(stack) != 0:
                    stack.pop()
            elif op != "./":
                stack.append(op)
        return len(stack)