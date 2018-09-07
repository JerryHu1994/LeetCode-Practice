class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        ptr = ind = 0
        while ind < len(abbr):
            if ptr >= len(word):    return False
            if abbr[ind].isdigit():
                num = ""
                if abbr[ind] == "0":    return False
                while ind < len(abbr) and abbr[ind].isdigit():
                    num += abbr[ind]
                    ind += 1
                num = int(num)
                ptr += num
            else:
                if word[ptr] != abbr[ind]:  return False
                ptr += 1
                ind += 1
        if ptr != len(word):    return False
        return True