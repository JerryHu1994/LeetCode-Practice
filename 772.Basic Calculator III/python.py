class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, ind = [], 0
        while ind < len(s):
            val = s[ind]
            if val == " ":
                ind += 1
                continue
            elif val == "+" or val == "-" or val == "*" or val == "/":
                # add all operators
                stack.append(val)
            elif val == "(":
                # find the entire parenthesis
                count = 1
                curr = ind+1
                while True:
                    if s[curr] == "(":  count += 1
                    if s[curr] == ")":  count -= 1
                    if count == 0:  break    
                    curr += 1
                stack.append(self.calculate(s[ind+1:curr]))
                ind = curr
            else:
                curr = ind
                while curr < len(s) and s[curr].isdigit():  curr += 1
                stack.append(int(s[ind:curr]))
                ind = curr
                continue
            ind += 1
        nextstack, ind = [], 0
        while len(stack):
            curr = stack.pop(0)
            if curr == "*":
                nextstack.append(nextstack.pop()*stack.pop(0))
            elif curr == "/":
                nextstack.append(nextstack.pop()//stack.pop(0))
            else:
                nextstack.append(curr)
        ret = nextstack[0]
        for i in range(1, len(nextstack), 2):
            if nextstack[i] == "+":
                ret += nextstack[i+1]
            else:
                ret -= nextstack[i+1]
        return ret