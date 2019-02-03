class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if not stack:   return False
                pre = stack.pop()
                if not((pre=='(' and i==')') or (pre=='{' and i=='}') or (pre=='[' and i==']')):    return False
        return True if len(stack)==0 else False
        