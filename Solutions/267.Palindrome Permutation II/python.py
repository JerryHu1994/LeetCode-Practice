class Solution(object):
    def helper(self, dic, li, l):
        if l == 0:
            self.ret.append(li + li[::-1])
        elif l == 1:
            for k in dic:
                if dic[k] == 1: self.ret.append(li + [k] + li[::-1])
        else:
            for k in dic:
                if dic[k] >= 2:
                    dic[k] -= 2
                    self.helper(dic, li+[k], l-2)
                    dic[k] += 2

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        dic = collections.defaultdict(int)
        for i in s: dic[i] += 1
        odd = False
        for k,v in dic.iteritems():
            if v%2 == 1:
                if odd:
                    return []
                else:
                    odd = True
        self.ret = []
        self.helper(dic, [], l)
        res = []
        for r in self.ret:  res.append("".join(r))
        return res