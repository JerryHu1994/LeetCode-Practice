class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        left_p = []
        for ind, char in enumerate(s):
            if char == "(":
                left_p.append(len(stack))
                stack.append(char)
            elif char == ")":
                last_p_ind = left_p.pop()
                stack = stack[:last_p_ind] + stack[last_p_ind+1:][::-1]
            else:
                stack.append(char)
        return "".join(stack)