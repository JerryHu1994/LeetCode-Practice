class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        reverse = "".join([i for i in S if i.isalpha()])[::-1]
        ret, ind = "", 0
        for i in S:
            if i.isalpha():
                ret += reverse[ind]
                ind += 1
            else:
                ret += i
        return ret