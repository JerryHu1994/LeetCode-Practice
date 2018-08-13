class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        diff = ord('a') - ord('A')
        ret = ""
        for i in str:
            if ord(i) >= ord('a') or not i.isalpha():
                ret += i
            else:
                ret += chr(ord(i)+diff)
        return ret