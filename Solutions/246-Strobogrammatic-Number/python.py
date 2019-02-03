class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {"6":"9", "9":"6", "8":"8", "1":"1", "0":"0"}
        rotated = ""
        for i in num[::-1]:
            if i in dic:
                rotated += dic[i]
            else:
                return False
        return rotated == num
        