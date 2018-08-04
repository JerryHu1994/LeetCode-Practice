class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        stack = []
        i = len(s)-1
        while i>=0:
            curr = s[i]
            if len(stack) and stack[-1] == "[":
                # capture the number
                endidx = i
                while i>=0 and s[i] in "0123456789":
                    i-=1
                currnum = int(s[i+1:endidx+1])
                stack.pop() # pop the [
                currstr = ""
                i+=1
                if i<0: break
                while stack[-1] != "]":
                    currstr+=stack.pop()
                stack.pop() # pop the ]
                stack.append(currstr*currnum)
            else:
                stack.append(curr)
            i-=1
        ret = ""
        for i in stack[::-1]:
            ret += i
        return ret
            
            
            