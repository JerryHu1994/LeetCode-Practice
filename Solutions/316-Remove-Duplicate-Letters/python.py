class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        ret, visited = [], [False]*26
        for i in s:
            ind = ord(i) - ord('a')
            counter[i] -= 1
            if visited[ind]:  continue
            # if the top one is larger and the remainings contains another top one
            while len(ret) and ord(i) < ord(ret[-1]) and counter[ret[-1]] > 0:
                visited[ord(ret.pop()) - ord('a')] = False
            ret.append(i)
            visited[ind] = True
        return "".join(ret)