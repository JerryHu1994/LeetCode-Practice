class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        last = 0
        for ind, val in enumerate(str):
            if val == " ":
                #reverse the current word
                temp = str[last:ind]
                temp.reverse()
                str[last:ind] = temp
                last = ind+1
        # reverse the last one
        laststr = str[last:]
        laststr.reverse()
        str[last:] = laststr
                