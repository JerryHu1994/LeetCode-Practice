class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        ret = ""
        for i in range(len(word_list)):
            newstr = word_list[i][::-1] if i == len(word_list)-1 else word_list[i][::-1] + " "
            ret+=newstr 
        return ret