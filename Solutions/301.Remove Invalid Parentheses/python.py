class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            currsum = 0
            for i in string:
                if i == "(":
                    currsum += 1
                elif i == ")":
                    currsum -= 1
                if currsum < 0: return False
            return currsum == 0
        # bfs
        queue, found, ret, visited = [s], False, [], set([s])
        if isValid(s):  return [s]
        while queue and not found:
            nextq = []
            for currs in queue:
                for i in range(len(currs)):
                    nextstr = currs[:i] + currs[i+1:]
                    if nextstr in visited:  continue
                    if isValid(nextstr):
                        found = True
                        ret.append(nextstr)
                    else:
                        nextq.append(nextstr)
                        visited.add(nextstr)
                if not found:   queue = nextq
        return list(set(ret))