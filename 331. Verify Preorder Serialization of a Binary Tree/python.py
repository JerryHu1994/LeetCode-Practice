class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(",")
        for c in preorder:
            stack.append(c)
            while len(stack) > 2:
                if stack[-1] == "#" and stack[-2] == "#":
                    stack.pop()
                    stack.pop()
                    if len(stack) == 0:
                        return False
                    parent = stack.pop()
                    if not parent.isdigit():
                        return False
                    stack.append("#")
                else:
                    break      
        return stack == ["#"]