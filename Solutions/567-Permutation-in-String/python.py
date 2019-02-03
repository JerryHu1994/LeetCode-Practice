class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ls1 = len(s1)
        dic = {}
        for i in s1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        l, r = -1, 0
        tempdic = dic.copy()
        while r < len(s2):
            char = s2[r]
            if not char in tempdic:
                # next char not in dic, shift left pointer to right
                l = r
                r+=1
                tempdic = dic.copy()
            elif tempdic[char] > 0:
                tempdic[char] -= 1
                if r - l == ls1:
                    return True
                r+=1
            else:
                # shift left pointer by one
                l += 1
                tempdic[s2[l]] += 1
        return False
        