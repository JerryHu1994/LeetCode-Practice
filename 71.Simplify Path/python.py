class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        splited, stack = path.split("/"), []
        for i in splited:
            if i=="" or i==".": continue
            stack.append(i)
        result = []
        for i in stack:
            if i=="..":
                if len(result):   result.pop()
            else:
                result.append(i)
        ret = ""
        for i in result:    ret += "/"+i
        return "/"+ret if len(ret)==0 else ret
            
        
        